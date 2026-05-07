from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .models import Artigo


AUTORES_GROUP_NAME = 'autores'


def get_autores_group():
    grupo, _ = Group.objects.get_or_create(name=AUTORES_GROUP_NAME)
    content_type = ContentType.objects.get_for_model(Artigo)
    permissoes = Permission.objects.filter(
        content_type=content_type,
        codename__in=[
            'add_artigo',
            'view_artigo',
            'change_artigo',
            'delete_artigo',
        ],
    )
    grupo.permissions.add(*permissoes)
    return grupo


def user_is_autor(user):
    return user.is_authenticated and user.groups.filter(name=AUTORES_GROUP_NAME).exists()
