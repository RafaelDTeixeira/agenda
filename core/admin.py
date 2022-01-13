from django.contrib import admin
from core.models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display=('id','titulo','data_evento','data_criacao','usuario','local')
    list_filter=('data_evento','titulo','usuario')
    ordering=('id',)


