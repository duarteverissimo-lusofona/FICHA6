from django.contrib import admin

from .models import MagicLoginToken


@admin.register(MagicLoginToken)
class MagicLoginTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'used')
    list_filter = ('used', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('token', 'created_at')

# No admin do Django, criar o grupo "gestor-portfolio" e atribuir permissoes
# add, view, change e delete para os modelos CRUD do portfolio: Projeto,
# Tecnologia, Competencia, Formacao e quaisquer outros modelos CRUD que venham
# a ser geridos por este grupo.
#
# Depois, criar/editar o utilizador gestor, associar ao grupo "gestor-portfolio"
# e marcar is_staff=True se esse utilizador tambem precisar de aceder ao admin.
