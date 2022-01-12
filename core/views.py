from sys import displayhook
from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def agendamento(resquest):
    usuario=resquest.user
    if str(usuario) is 'AnonymousUser':
        return redirect('/')

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

@login_required(login_url='login/')
def index(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuario=authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,'Usuário ou senha inválidos')

    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')
    