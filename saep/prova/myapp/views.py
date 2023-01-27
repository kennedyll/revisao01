from calendar import c
from plistlib import UID
from django.shortcuts import render, redirect, HttpResponse
from myapp.forms import UsersForm, LoginForm, AgendamentoForm
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
            return redirect('login')
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'cadastro.html')

def erro(request):
    return render(request, 'erro.html')

def servico(request):
    try:
        profile = {}
        profile['uid'] = Usuario.objects.get(id=request.session['uid'])
        return render(request,'servico.html', profile)
    except:
        return render(request,'home.html')

def contato(request):
    return render(request, 'contato.html')

def agendamento(request):
    data = {}
    if request.method == 'POST':
            data_convertida = datetime.strptime(request.POST['data'], '%Y-%m-%d').date()
            if data_convertida < datetime.now().date():
                c = Agendamento(usuario=Usuario.objects.get(id=request.session['uid']), nome = request.POST['nome'], data = request.POST['data'], horario = request.POST['horario'], servico = request.POST['servico'], funcionario = request.POST['funcionario'],  endereco = request.POST['endereco'])
                c.save()
            return redirect('servico')
    else:
        data['agendform'] = AgendamentoForm()

        return render(request,'agendamento.html', data)
    

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)

def dolog(request):
    if request.method == 'POST':
        try:
            user = Usuario.objects.get(usuario=request.POST['usuario']) # select * from usuario where usuario
            print(user)
        except:
            return HttpResponse("Falha no Login")
        if user.senha == request.POST['senha']:
            request.session['uid'] = user.id
            return redirect('servico')
        else:
            return HttpResponse("servico")
    else:
        redirect('cadastro')

def dologout(request):
    if request.session['uid'] != "" or request.session['uid'] != None:
        try:
            del request.session['uid']
        except KeyError:
            return redirect('home')
    return redirect('home')


