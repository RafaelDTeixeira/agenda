from django.contrib import admin
from core.models import Evento, Pessoa

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display=('titulo','data_evento','data_criacao')

@admin.register(Pessoa)  
class PessoaAdmin(admin.ModelAdmin):
    list_display=('nome','idade','rg','endereco')

