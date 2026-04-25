from django.urls import path

from . import views


urlpatterns = [
    path("", views.portfolio_view, name="portfolio_home"),
    path("licenciaturas/", views.licenciaturas_view, name="portfolio_licenciaturas"),
    path("docentes/", views.docentes_view, name="portfolio_docentes"),
    path("disciplinas/", views.disciplinas_view, name="portfolio_disciplinas"),
    path("tecnologias/", views.tecnologias_view, name="portfolio_tecnologias"),
    path("projetos/", views.projetos_view, name="portfolio_projetos"),
    path("tfcs/", views.tfcs_view, name="portfolio_tfcs"),
    path("competencias/", views.competencias_view, name="portfolio_competencias"),
    path("formacoes/", views.formacoes_view, name="portfolio_formacoes"),
    path("experiencias/", views.experiencias_view, name="portfolio_experiencias"),
    path("making-of/", views.making_of_view, name="portfolio_making_of"),
]
