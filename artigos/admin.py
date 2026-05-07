from django.contrib import admin

from .models import Artigo, Comentario, Like


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'total_likes')
    list_filter = ('data_criacao', 'autor')
    search_fields = ('titulo', 'texto', 'autor__username')

    def total_likes(self, obj):
        return obj.likes.count()

    total_likes.short_description = 'Likes'


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'data_criacao')
    list_filter = ('data_criacao', 'autor')
    search_fields = ('texto', 'artigo__titulo', 'autor__username')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'user', 'session_key', 'data_criacao')
    list_filter = ('data_criacao',)
    search_fields = ('artigo__titulo', 'user__username', 'session_key')
