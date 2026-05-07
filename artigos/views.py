from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ArtigoForm, ComentarioForm
from .models import Artigo, Like
from .utils import user_is_autor


def lista_artigos(request):
    artigos = (
        Artigo.objects.select_related('autor')
        .annotate(total_likes=Count('likes'))
        .order_by('-data_criacao')
    )

    return render(
        request,
        'artigos/lista_artigos.html',
        {
            'artigos': artigos,
            'user_is_autor': user_is_autor(request.user),
        },
    )


def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(
        Artigo.objects.select_related('autor'),
        id=artigo_id,
    )
    comentarios = artigo.comentarios.select_related('autor')
    comentario_form = ComentarioForm()

    liked = False
    if request.user.is_authenticated:
        liked = artigo.likes.filter(user=request.user).exists()
    elif request.session.session_key:
        liked = artigo.likes.filter(
            user__isnull=True,
            session_key=request.session.session_key,
        ).exists()

    return render(
        request,
        'artigos/detalhe_artigo.html',
        {
            'artigo': artigo,
            'comentarios': comentarios,
            'comentario_form': comentario_form,
            'likes_count': artigo.likes.count(),
            'liked': liked,
            'pode_editar': user_is_autor(request.user) and request.user == artigo.autor,
        },
    )


@login_required
def criar_artigo(request):
    if not user_is_autor(request.user):
        return HttpResponseForbidden("Nao tem permissao para criar artigos.")

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('detalhe_artigo', artigo_id=artigo.id)

    return render(
        request,
        'artigos/form_artigo.html',
        {
            'form': form,
            'titulo_pagina': 'Criar artigo',
            'texto_botao': 'Criar artigo',
        },
    )


@login_required
def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if not user_is_autor(request.user):
        return HttpResponseForbidden("Nao tem permissao para editar artigos.")

    if artigo.autor != request.user:
        return HttpResponseForbidden("Nao pode editar artigos de outro autor.")

    form = ArtigoForm(
        request.POST or None,
        request.FILES or None,
        instance=artigo,
    )

    if form.is_valid():
        form.save()
        return redirect('detalhe_artigo', artigo_id=artigo.id)

    return render(
        request,
        'artigos/form_artigo.html',
        {
            'form': form,
            'artigo': artigo,
            'titulo_pagina': 'Editar artigo',
            'texto_botao': 'Guardar alteracoes',
        },
    )


@require_POST
def like_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.user.is_authenticated:
        like = Like.objects.filter(artigo=artigo, user=request.user).first()
        if like:
            like.delete()
        else:
            Like.objects.create(artigo=artigo, user=request.user)
    else:
        if not request.session.session_key:
            request.session.save()

        like = Like.objects.filter(
            artigo=artigo,
            user__isnull=True,
            session_key=request.session.session_key,
        ).first()
        if like:
            like.delete()
        else:
            Like.objects.create(
                artigo=artigo,
                session_key=request.session.session_key,
            )

    return redirect('detalhe_artigo', artigo_id=artigo.id)


@login_required
@require_POST
def comentar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    form = ComentarioForm(request.POST)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.autor = request.user
        comentario.save()

    return redirect('detalhe_artigo', artigo_id=artigo.id)
