from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, ExperienciaProfissional, MakingOf


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'departamento')
    list_filter = ('departamento',)
    search_fields = ('nome', 'sigla')


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ects')
    search_fields = ('nome', 'sigla')


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel_interesse')
    list_filter = ('tipo',)
    search_fields = ('nome',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano')
    search_fields = ('titulo', 'descricao')


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'area_tematica', 'nivel_interesse')
    search_fields = ('titulo', 'resumo', 'area_tematica')


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel')
    list_filter = ('categoria',)
    search_fields = ('nome',)


@admin.register(ExperienciaProfissional)
class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'tipo', 'data_inicio', 'data_fim')
    list_filter = ('tipo', 'empresa')
    search_fields = ('cargo', 'empresa')


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_registo', 'entidade_referida')
    list_filter = ('data_registo',)
    search_fields = ('titulo', 'descricao', 'entidade_referida')