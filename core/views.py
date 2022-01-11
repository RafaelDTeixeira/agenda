from sys import displayhook
from django.shortcuts import render,HttpResponse

from core.models import Evento

def agendamento(resquest):
    usuario=resquest.user
    evento=Evento.objects.filter(usuario=usuario)
    usuario=str(usuario).capitalize
    
    dados={'eventos':evento,'usuario':usuario}
    return render(resquest,'agenda.html',dados)

def titulo(resquest,titulo_evento):
    print(titulo_evento)
    usuario=resquest.user
    consulta=Evento.objects.get(titulo__contains=titulo_evento)
    usuario=str(usuario).capitalize

    dados={'consulta':consulta,'usuario':usuario}
    return render(resquest,'titulo.html',dados)