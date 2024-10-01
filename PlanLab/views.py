from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Aula, Usuario

def login_view(request):
    if request.method =="POST":
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})
        
    return render(request, "login.html")
