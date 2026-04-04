from django.contrib import admin

# Register your models here.
from .models import Licenciatura, Docente


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla','departamento')
    list_filter = ('departamento',)
    search_fields = ('nome', 'sigla')


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'departamento')
    search_fields = ('nome', 'email')
    list_filter = ('departamento',)
