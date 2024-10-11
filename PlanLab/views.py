from django.shortcuts import render, redirect
from .models import Aula, Caderneta
from .forms import CadernetaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def pag_planos_de_aula(request):
    aulas = Aula.objects.all()
    return render(request, 'pag_planos_de_aula.html', {'aulas': aulas})


@login_required
def form_aula(request):
    if request.method == 'POST':
        disciplina = request.POST['disciplina']
        data_aula = request.POST['data']  # Renomeado para data_aula
        turma = request.POST['serie']      # Renomeado para turma
        semestre = request.POST['semestre']
        titulo = request.POST['titulo']
        eventos_extraordinarios = request.POST.get('eventos', '')  # Renomeado
        conteudo_programatico = request.POST['conteudo']  # Renomeado
        metodologia = request.POST['metodologia']
        recursos_necessarios = request.POST['recursos']  # Renomeado
        avaliacao_observacoes = request.POST.get('avaliacao', '')  # Renomeado
        observacoes = request.POST.get('observacao', '')  # Renomeado

        # Crie a instância do modelo e salve no banco de dados
        Aula.objects.create(
            disciplina=disciplina,
            data_aula=data_aula,  # Correção
            turma=turma,          # Correção
            semestre=semestre,
            titulo=titulo,
            eventos_extraordinarios=eventos_extraordinarios,  # Correção
            conteudo_programatico=conteudo_programatico,  # Correção
            metodologia=metodologia,
            recursos_necessarios=recursos_necessarios,  # Correção
            avaliacao_observacoes=avaliacao_observacoes,  # Correção
            observacoes=observacoes,  # Correção
            usuario=request.user  # Adicionando o usuário logado
        )

        messages.success(request, 'Plano de aula salvo com sucesso!')
        return redirect('pag_planos_de_aula')  # Redireciona para a página de planos de aula

    return render(request, 'form_aula.html')


@login_required
def pag_cadernetas(request):
    cadernetas = Caderneta.objects.filter(usuario=request.user)
    return render(request, 'pag_cadernetas.html', {'cadernetas': cadernetas})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CadernetaForm  # Certifique-se de que o formulário está importado corretamente

@login_required
def form_caderneta(request):
    if request.method == 'POST':
        form = CadernetaForm(request.POST)
        if form.is_valid():
            caderneta = form.save(commit=False)
            caderneta.usuario = request.user  # Preenchendo o campo usuário
            caderneta.save()
            return redirect('caderneta_list')  # Redirecionar para uma lista de cadernetas, por exemplo
    else:
        form = CadernetaForm()
    
    return render(request, 'form_caderneta.html', {'form': form})






@login_required
def login_view(request):
    return render(request, 'login.html')


@login_required
def cadastro(request):
    return render(request, 'cadastro.html')


@login_required
def caderneta(request):
    return render(request, 'caderneta.html')


@login_required
def plano(request):
    return render(request, 'plano.html')
