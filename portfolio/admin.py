from django.contrib import admin

# Register your models here.
from .models import Licenciatura

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'grau', 'departamento')
    list_filter = ('grau', 'departamento')
    search_fields = ('nome', 'sigla')

