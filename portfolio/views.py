from django.shortcuts import render

from .models import (
    Competencia,
    Docente,
    ExperienciaProfissional,
    Formacao,
    Licenciatura,
    MakingOf,
    Projeto,
    Tecnologia,
    TFC,
    UnidadeCurricular,
)


def portfolio_view(request):
    return render(request, "portfolio/index.html")


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


def projetos_view(request):
    projetos = Projeto.objects.select_related("uc").prefetch_related(
        "tecnologias",
    ).order_by("-ano", "titulo")

    return render(request, "portfolio/projetos.html", {"projetos": projetos})


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


def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related("competencias").order_by(
        "-data_inicio",
        "titulo",
    )

    return render(request, "portfolio/formacoes.html", {"formacoes": formacoes})


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
