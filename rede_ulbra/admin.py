from django.contrib import admin
from .models import Comentario,Curtidas,Perfil,User

@admin.register(Comentario)
class comentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','coment']

@admin.register(Curtidas)
class CurtidasAdmin(admin.ModelAdmin):
    list_display = ['emog','pessoa']

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario','descricao','telefone',
    'cidade','foto','email']
# Register your models here.
