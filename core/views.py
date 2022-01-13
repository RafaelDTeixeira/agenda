from sys import displayhook
from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def agendamento(request):
    usuario=request.user
    if str(usuario) is 'AnonymousUser':
        return redirect('/')

    evento=Evento.objects.filter(usuario=usuario)
    usuario=str(usuario).capitalize

    dados={'eventos':evento,'usuario':usuario}
    return render(request,'agenda.html',dados)

@login_required(login_url='/login/')
def evento(request):    
    id_evento=request.GET.get('id')
    if id_evento:
        print(id_evento)
        usuario=Evento.objects.get(id=id_evento)
        print(usuario)
        context={'dados':usuario}
        return render(request,'evento.html',context)
    return render(request,'evento.html')

@login_required(login_url='/login/')
def evento_submit(request):
    if request.POST:
        titulo=request.POST.get('titulo')
        data_evento=request.POST.get('data_evento')
        descricao=request.POST.get('descricao')
        local=request.POST.get('local')
        usuario=request.user
        id_evento=request.POST.get("id_evento")
        evento=Evento.objects.get(id=id_evento)
        if id_evento and evento.usuario==usuario:
            try:            
                Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                            data_evento=data_evento,
                                                            descricao=descricao)
                
            except ConnectionRefusedError:
                messages.error(request,'Falha na solicitação.')
            
        else:
            try:
                Evento.objects.update_or_create(titulo=titulo,
                                            data_evento=data_evento,
                                            descricao=descricao,
                                            usuario=usuario,local=local)
            except ConnectionRefusedError:
                messages.error(request,'Falha na solicitação.')
                return redirect('agenda/evento')        

    return redirect('/agenda')


@login_required(login_url='/login/')
def delete_evento(request,id_evento):
    usuario=request.user
    evento=Evento.objects.get(id=id_evento) # Evento.objects.filter(id=id_evento).delete()

    if usuario==evento.usuario:
        evento.delete()
    return redirect('/')

def titulo(resquest,id):
    print(id)
    usuario=resquest.user
    consulta=Evento.objects.get(id=id)
    print(consulta)
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
