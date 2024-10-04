from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'planlab/login.html')

def cadastro(request):
    return render(request, 'planlab/cadastro.html')

def caderneta(request):
    return render(request, 'planlab/caderneta.html')

def form(request):
    return render(request, 'planlab/form.html')

def plano(request):
    return render(request, 'planlab/plano.html')
