from django.shortcuts import render, redirect, get_object_or_404
from .models import Aula, Caderneta, Disciplina, Turma, Semestre
from .forms import CadernetaForm, AulaForm
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
def plano(request, id):
    plano = get_object_or_404(Aula, id=id) 
    return render(request, 'plano.html', {'plano': plano})


@login_required
def form_aula(request):
    if request.method == 'POST':
        form_data = {
            'disciplina': Disciplina.objects.get(id=request.POST['disciplina']),
            'data_aula': request.POST['data'],
            'turma': Turma.objects.get(id=request.POST['serie']),
            'semestre': Semestre.objects.get(id=request.POST['semestre']),
            'titulo': request.POST['titulo'],
            'eventos_extraordinarios': request.POST.get('eventos', ''),
            'conteudo_programatico': request.POST['conteudo_programatico'],
            'metodologia': request.POST['metodologia'],
            'recursos_necessarios': request.POST['recursos_necessarios'],
            'avaliacao_observacoes': request.POST.get('avaliacao_observacoes', ''),
            'observacoes': request.POST.get('observacao', ''),
            'usuario': request.user  # Adicionando o usuário logado
        }

        Aula.objects.create(**form_data)

        messages.success(request, 'Plano de aula salvo com sucesso!')
        return redirect('pag_planos_de_aula')

    disciplinas = Disciplina.objects.all()
    turmas = Turma.objects.all()
    semestres = Semestre.objects.all()

    return render(request, 'form_aula.html', {
        'disciplinas': disciplinas,
        'turmas': turmas,
        'semestres': semestres,
    })


@login_required
def form_editar_aula(request, plano_id):
    plano = get_object_or_404(Aula, id=plano_id)  # Obtém o plano de aula existente

    if request.method == 'POST':
        form = AulaForm(request.POST, instance=plano)  # Atualiza os dados com a instância do plano
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            messages.success(request, 'Plano de aula atualizado com sucesso!')  # Mensagem de sucesso
            return redirect('plano', id=plano_id)  # Redireciona para a página de detalhes do plano de aula
        else:
            # Se o formulário não for válido, exibe mensagens de erro
            messages.error(request, 'Erro ao atualizar o plano de aula. Verifique os campos e tente novamente.')
    else:
        form = AulaForm(instance=plano)  # Pré-preenche o formulário com os dados do plano existente

    return render(request, 'form_editar_aula.html', {'form': form, 'plano': plano})



@login_required
def excluir_plano(request, plano_id):
    plano = get_object_or_404(Aula, id=plano_id)
    
    if request.method == 'POST':
        plano.delete()
        return redirect('pag_planos_de_aula')  # Redireciona para a página pag_planos
    else:
        # Se não for um POST, você pode redirecionar ou lidar de outra forma.
        return redirect('pag_planos_de_aula')  # Você pode adicionar uma mensagem de erro aqui, se desejar.
    



    

@login_required
def caderneta(request, id):
    caderneta = get_object_or_404(Caderneta, id=id)
    return render(request, 'caderneta.html', {'caderneta': caderneta})



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
            caderneta.usuario = request.user 
            caderneta.save()
            messages.success(request, 'Caderneta salva com sucesso!')
            return redirect('pag_cadernetas')
    else:
        form = CadernetaForm()

    return render(request, 'form_caderneta.html', {
        'form': form,
        'disciplinas': disciplinas,
        'series': series,
        'periodos': periodos
    })

@login_required
def form_editar_caderneta(request, caderneta_id):
    caderneta = get_object_or_404(Caderneta, id=caderneta_id)

    if request.method == 'POST':
        form = CadernetaForm(request.POST, instance=caderneta)  # Atualizar a caderneta existente
        if form.is_valid():
            form.save()
            messages.success(request, 'Caderneta atualizada com sucesso!')
            return redirect('caderneta', id=caderneta_id)  # Redirecionar após salvar
    else:
        form = CadernetaForm(instance=caderneta)  # Carregar dados existentes no formulário

    return render(request, 'form_editar_caderneta.html', {'form': form, 'caderneta': caderneta})



@login_required
def excluir_caderneta(request, id):
    caderneta = get_object_or_404(Caderneta, id=id)
    if request.method == 'POST':
        caderneta.delete()
        return redirect('pag_cadernetas')  # Redireciona para a página pag_cadernetas
    else:
        # Se não for um POST, você pode redirecionar ou lidar de outra forma.
        return redirect('pag_cadernetas')  # Você pode adicionar uma mensagem de erro aqui, se desejar.




@login_required
def login_view(request):
    return render(request, 'login.html')


@login_required
def cadastro(request):
    return render(request, 'cadastro.html')


