from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.]
"""
def index(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/manager_page/')   
    else:
        data['msg'] = 'Usuário ou senha inválidos'
        data['class'] = 'alert-danger'
        return render(request, 'index.html', data)
"""
def main(request):
    return render(request, 'main.html')

# Formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')

#Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
        
    return render(request, 'create.html', data)

def index(request):
    return render(request, 'index.html')

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/manager_page/')   
    else:
        data['msg'] = 'Usuário ou senha inválidos'
        data['class'] = 'alert-danger'
        return render(request, 'index.html', data)

#TODO arrumar index e o redirecionamento para a manager page
#TODO voltar a usar bootstrap? Ele n está pegando os dados preenchidos nas caixas de texto

def manager_page(request):
    return render(request, 'manager_page.html')