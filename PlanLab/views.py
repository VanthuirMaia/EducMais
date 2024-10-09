from django.shortcuts import render, redirect
from .models import Aula


def home(request):
    return render(request, 'home.html')

def planos_de_aula(request):
    aulas = Aula.objects.all()
    return render(request, 'planos_de_aula.html', {'aulas': aulas})


def pag_cadernetas(request):
    return render(request, 'pag_cadernetas.html')






def login_view(request):
    return render(request, '/login.html')

def cadastro(request):
    return render(request, '/cadastro.html')

def caderneta(request):
    return render(request, '/caderneta.html')

def form(request):
    return render(request, '/form.html')

def plano(request):
    return render(request, '/plano.html')
