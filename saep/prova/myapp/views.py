from calendar import c
from plistlib import UID
from django.shortcuts import render, redirect, HttpResponse
from myapp.forms import UsersForm, LoginForm
from myapp.models import Usuario, Agendamento
from datetime import datetime

# Create your views here.

def home(request):
    tabela = Usuario.objects.all()
    return render(request, 'home.html',{'usuario':tabela})

def login(request):
    data = {}
    data['login'] = LoginForm()
    return render(request, 'login.html', data)

def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    print(form)
    for c in tabela:
        if form['usuario'].data == c.usuario:
            return redirect('erro')
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'cadastro.html')

def erro(request):
    return render(request, 'erro.html')

def servico(request):
    return render(request, 'servico.html')

def agendamento(request):
    if request.method == 'POST':
            c = Agendamento(usuario=Usuario.objects.get(id=request.session['uid']), nome = request.POST['nome'], ultimo_nome = request.POST['ultimo_nome'], celular = request.POST['celular'], data = request.POST['data'], hora = request.POST['hora'], comentario = request.POST['comentario'])
            data_convertida = datetime.strptime(request.POST['data'], '%Y-%m-%d').date()
            if data_convertida < datetime.now().date():
                    return redirect('erroagend')
            else:
                c.save()

    return render(request, 'agendamento.html')

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)

def dolog(request):
    if request.method == 'POST':
        try:
            user = Usuario.objects.get(usuario=request.POST['usuario']) # select * from usuario where usuario
        except:
            return HttpResponse("Falha no Login")
        print(user)
        if user.senha == request.POST['senha']:
            request.session['uid'] = user.id
            return redirect('home')
        else:
            return HttpResponse("Falha no Login")
    else:
        redirect('cadastro')


