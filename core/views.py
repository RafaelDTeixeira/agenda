from django.shortcuts import render,HttpResponse

from core.models import Evento

def agendamento(resquest):
    evento=Evento.objects.all()
    dados={'eventos':evento}
    return render(resquest,'agenda.html',dados)

def titulo(resquest,titulo_evento):
    consulta=Evento.objects.get(titulo=titulo_evento)
    dados={'consulta':consulta}
    return render(resquest,'titulo.html',dados)