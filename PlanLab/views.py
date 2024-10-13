from django.shortcuts import render, redirect, get_object_or_404
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
        # Coletando dados do formulário
        form_data = {
            'disciplina': request.POST['disciplina'],
            'data_aula': request.POST['data'],
            'turma': request.POST['serie'],
            'semestre': request.POST['semestre'],
            'titulo': request.POST['titulo'],
            'eventos_extraordinarios': request.POST.get('eventos', ''),
            'conteudo_programatico': request.POST['conteudo'],
            'metodologia': request.POST['metodologia'],
            'recursos_necessarios': request.POST['recursos'],
            'avaliacao_observacoes': request.POST.get('avaliacao', ''),
            'observacoes': request.POST.get('observacao', ''),
            'usuario': request.user  # Adicionando o usuário logado
        }
        
        # Cria a instância do modelo e salva no banco de dados
        Aula.objects.create(**form_data)

        messages.success(request, 'Plano de aula salvo com sucesso!')
        return redirect('pag_planos_de_aula')

    return render(request, 'form_aula.html')


@login_required
def pag_cadernetas(request):
    cadernetas = Caderneta.objects.filter(usuario=request.user)
    return render(request, 'pag_cadernetas.html', {'cadernetas': cadernetas})


@login_required
def form_caderneta(request):
    disciplinas = ['Matemática', 'Português', 'Ciências', 'Física']
    series = ['1º Ano - Fundamental', '2º Ano - Fundamental', '3º Ano - Fundamental', '1º Ano - Médio']
    periodos = ['1º Semestre', '2º Semestre', '3º Semestre']

    if request.method == 'POST':
        form = CadernetaForm(request.POST)
        if form.is_valid():
            caderneta = form.save(commit=False)
            caderneta.usuario = request.user  # Preenchendo o campo usuário
            caderneta.save()
            messages.success(request, 'Caderneta salva com sucesso!')
            return redirect('pag_cadernetas')  # Redirecionar para a lista de cadernetas
    else:
        form = CadernetaForm()

    return render(request, 'form_caderneta.html', {
        'form': form,
        'disciplinas': disciplinas,
        'series': series,
        'periodos': periodos
    })


def plano(request, id):
    aula = get_object_or_404(Aula, id=id)  # Busca a aula com base no ID
    return render(request, 'plano.html', {'plano': aula})  # Alterado para 'plano'



@login_required
def login_view(request):
    return render(request, 'login.html')


@login_required
def cadastro(request):
    return render(request, 'cadastro.html')


@login_required
def caderneta(request):
    return render(request, 'caderneta.html')

