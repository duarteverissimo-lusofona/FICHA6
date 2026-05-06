from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CompetenciaForm, FormacaoForm, ProjetoForm, TecnologiaForm

from .models import (
    Competencia,
    Docente,
    ExperienciaProfissional,
    Formacao,
    Licenciatura,
    MakingOf,
    Projeto,
    Tecnologia,
    TipoTecnologia,
    TFC,
    UnidadeCurricular,
)


def portfolio_view(request):
    return render(request, "portfolio/index.html")


def sobre_aplicacao_view(request):
    tecnologias_query = Tecnologia.objects.prefetch_related("projetos").order_by("nome")
    tipos_tecnologia = TipoTecnologia.objects.prefetch_related(
        Prefetch(
            "tecnologias",
            queryset=tecnologias_query,
            to_attr="tecnologias_ordenadas",
        ),
    ).order_by("nome")
    tipos_com_tecnologias = [
        tipo for tipo in tipos_tecnologia if tipo.tecnologias_ordenadas
    ]

    return render(
        request,
        "portfolio/sobre_aplicacao.html",
        {"tipos_tecnologia": tipos_com_tecnologias},
    )


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related("ucs").order_by("nome")

    return render(
        request,
        "portfolio/licenciaturas.html",
        {"licenciaturas": licenciaturas},
    )


def docentes_view(request):
    docentes = Docente.objects.prefetch_related("ucs", "tfcs_orientados").order_by("nome")

    return render(request, "portfolio/docentes.html", {"docentes": docentes})


def disciplinas_view(request):
    disciplinas = UnidadeCurricular.objects.prefetch_related(
        "licenciaturas",
        "docentes",
    ).order_by("nome")

    return render(
        request,
        "portfolio/disciplinas.html",
        {"disciplinas": disciplinas},
    )


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.prefetch_related(
        "projetos",
        "tfcs",
        "experiencias",
    ).order_by("nome")

    return render(
        request,
        "portfolio/tecnologias.html",
        {"tecnologias": tecnologias},
    )


def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_tecnologias")

    return render(request, "portfolio/nova_tecnologia.html", {"form": form})


def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(
        request.POST or None,
        request.FILES or None,
        instance=tecnologia,
    )

    if form.is_valid():
        form.save()
        return redirect("portfolio_tecnologias")

    return render(
        request,
        "portfolio/edita_tecnologia.html",
        {"form": form, "tecnologia": tecnologia},
    )


def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == "POST":
        tecnologia.delete()
        return redirect("portfolio_tecnologias")

    return render(
        request,
        "portfolio/apaga_tecnologia.html",
        {"tecnologia": tecnologia},
    )


def projetos_view(request):
    projetos = Projeto.objects.select_related("uc").prefetch_related(
        "tecnologias",
    ).order_by("-ano", "titulo")

    return render(request, "portfolio/projetos.html", {"projetos": projetos})


def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_projetos")

    return render(request, "portfolio/novo_projeto.html", {"form": form})


def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)

    if form.is_valid():
        form.save()
        return redirect("portfolio_projetos")

    return render(
        request,
        "portfolio/edita_projeto.html",
        {"form": form, "projeto": projeto},
    )


def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == "POST":
        projeto.delete()
        return redirect("portfolio_projetos")

    return render(request, "portfolio/apaga_projeto.html", {"projeto": projeto})


def tfcs_view(request):
    tfcs = TFC.objects.select_related("licenciatura").prefetch_related(
        "orientadores",
        "tecnologias",
    ).order_by("-ano", "titulo")

    return render(request, "portfolio/tfcs.html", {"tfcs": tfcs})


def competencias_view(request):
    competencias = Competencia.objects.prefetch_related(
        "projetos",
        "formacoes",
    ).order_by("categoria", "nome")

    return render(
        request,
        "portfolio/competencias.html",
        {"competencias": competencias},
    )


def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_competencias")

    return render(request, "portfolio/nova_competencia.html", {"form": form})


def edita_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(
        request.POST or None,
        request.FILES or None,
        instance=competencia,
    )

    if form.is_valid():
        form.save()
        return redirect("portfolio_competencias")

    return render(
        request,
        "portfolio/edita_competencia.html",
        {"form": form, "competencia": competencia},
    )


def apaga_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)

    if request.method == "POST":
        competencia.delete()
        return redirect("portfolio_competencias")

    return render(
        request,
        "portfolio/apaga_competencia.html",
        {"competencia": competencia},
    )


def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related("competencias").order_by(
        "-data_inicio",
        "titulo",
    )

    return render(request, "portfolio/formacoes.html", {"formacoes": formacoes})


def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_formacoes")

    return render(request, "portfolio/nova_formacao.html", {"form": form})


def edita_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=formacao)

    if form.is_valid():
        form.save()
        return redirect("portfolio_formacoes")

    return render(
        request,
        "portfolio/edita_formacao.html",
        {"form": form, "formacao": formacao},
    )


def apaga_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)

    if request.method == "POST":
        formacao.delete()
        return redirect("portfolio_formacoes")

    return render(request, "portfolio/apaga_formacao.html", {"formacao": formacao})


def experiencias_view(request):
    experiencias = ExperienciaProfissional.objects.prefetch_related(
        "tecnologias",
        "competencias",
    ).order_by("-data_inicio", "empresa")

    return render(
        request,
        "portfolio/experiencias.html",
        {"experiencias": experiencias},
    )


def making_of_view(request):
    registos = MakingOf.objects.order_by("-data_registo", "titulo")

    return render(request, "portfolio/making_of.html", {"registos": registos})
