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
    query = request.GET.get('q', '')  # Pega o parâmetro 'q' da URL (se houver)
    
    if query:
        # Se houver uma busca, filtra os planos de aula com base no título
        aulas = Aula.objects.filter(titulo__icontains=query)
    else:
        # Se não houver busca, retorna todos os planos de aula
        aulas = Aula.objects.all()

    return render(request, 'pag_planos_de_aula.html', {
        'aulas': aulas,  # Passa os planos de aula para o template
        'query': query   # Passa o termo de busca para manter o campo preenchido
    })

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
def copiar_plano(request, id):
    aula_original = get_object_or_404(Aula, id=id)
    
    # Criação de uma cópia do plano de aula
    aula_copiada = Aula.objects.create(
        disciplina=aula_original.disciplina,
        data_aula=aula_original.data_aula,
        turma=aula_original.turma,
        semestre=aula_original.semestre,
        titulo=aula_original.titulo,
        eventos_extraordinarios=aula_original.eventos_extraordinarios,
        conteudo_programatico=aula_original.conteudo_programatico,
        metodologia=aula_original.metodologia,
        recursos_necessarios=aula_original.recursos_necessarios,
        avaliacao_observacoes=aula_original.avaliacao_observacoes,
        observacoes=aula_original.observacoes,
        usuario=request.user  # Garantir que a cópia seja associada ao usuário logado
    )
    
    messages.success(request, 'Plano de aula copiado com sucesso! Você pode agora editar os campos necessários.')
    return redirect('form_editar_aula', plano_id=aula_copiada.id)


def buscar_planos(request):
    query = request.GET.get('q', '')  # Pega o parâmetro de busca da URL
    planos = Aula.objects.all()  # Recupera todos os planos de aula

    if query:  # Se houver um termo de busca
        planos = planos.filter(titulo__icontains=query)  # Filtra os planos de aula pelo título

    return render(request, 'planlab/pag_planos_de_aula.html', {  # Corrija para o caminho correto
        'planos': planos,
        'query': query
    })



@login_required
def caderneta(request, id):
    caderneta = get_object_or_404(Caderneta, id=id)
    return render(request, 'caderneta.html', {'caderneta': caderneta})



@login_required
def pag_cadernetas(request):
    cadernetas = Caderneta.objects.filter(usuario=request.user)
    return render(request, 'pag_cadernetas.html', {'cadernetas': cadernetas})


@login_required
def form_caderneta(request, id=None):
    if id:
        caderneta = get_object_or_404(Caderneta, id=id)  # Editar
    else:
        caderneta = None  # Criar nova caderneta

    if request.method == 'POST':
        form_data = {
            'disciplina': Disciplina.objects.get(id=request.POST['disciplina']),
            'data_aula': request.POST['data_aula'],
            'turma': Turma.objects.get(id=request.POST['turma']),
            'semestre': Semestre.objects.get(id=request.POST['semestre']),
            'titulo': request.POST['titulo'],
            'eventos': request.POST.get('eventos', ''),  # Verifique se eventos é um campo de escolha
            'conteudo': request.POST['conteudo'],
            'materiais': request.POST.get('materiais', ''),
            'atividade': request.POST.get('atividade', ''),
            'usuario': request.user  # Usuário logado
        }

        if caderneta:  # Se for para editar a caderneta
            for field, value in form_data.items():
                setattr(caderneta, field, value)
            caderneta.save()
            messages.success(request, 'Caderneta atualizada com sucesso!')
        else:  # Se for para criar uma nova caderneta
            Caderneta.objects.create(**form_data)
            messages.success(request, 'Caderneta salva com sucesso!')

        return redirect('pag_cadernetas')  # Substitua pelo nome correto da sua URL de listagem

    context = {
        'caderneta': caderneta,
        'disciplinas': Disciplina.objects.all(),
        'turmas': Turma.objects.all(),
        'semestres': Semestre.objects.all(),
    }

    return render(request, 'form_caderneta.html', context)


@login_required
def form_editar_caderneta(request, caderneta_id):
    caderneta = get_object_or_404(Caderneta, id=caderneta_id)  # Obtém a caderneta existente

    if request.method == 'POST':
        form = CadernetaForm(request.POST, instance=caderneta)  # Atualiza os dados com a instância da caderneta
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            messages.success(request, 'Caderneta atualizada com sucesso!')  # Mensagem de sucesso
            return redirect('caderneta', id=caderneta_id)  # Redireciona para a página de detalhes da caderneta
        else:
            # Se o formulário não for válido, exibe mensagens de erro
            messages.error(request, 'Erro ao atualizar a caderneta. Verifique os campos e tente novamente.')
    else:
        form = CadernetaForm(instance=caderneta)  # Pré-preenche o formulário com os dados da caderneta existente

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
def copiar_caderneta(request, id):
    caderneta = get_object_or_404(Caderneta, id=id)  # Obtém a caderneta existente

    # Cria uma cópia da caderneta
    caderneta_copiada = Caderneta.objects.create(
        data_aula=caderneta.data_aula,
        disciplina=caderneta.disciplina,
        turma=caderneta.turma,
        semestre=caderneta.semestre,
        titulo=f'Cópia - {caderneta.titulo}',
        eventos=caderneta.eventos,
        conteudo=caderneta.conteudo,
        materiais=caderneta.materiais,
        atividade=caderneta.atividade,
        usuario=request.user  # A caderneta será associada ao usuário logado
    )

    messages.success(request, 'Caderneta copiada com sucesso! Você pode agora editar os campos necessários.')
    return redirect('form_editar_caderneta', caderneta_id=caderneta_copiada.id)

@login_required
def buscar_cadernetas(request):
    query = request.GET.get('q', '')  # Pega o parâmetro de busca da URL
    cadernetas = Caderneta.objects.all()  # Recupera todos os planos de aula

    if query:  # Se houver um termo de busca
        cadernetas = cadernetas.filter(titulo__icontains=query)  # Filtra os planos de aula pelo título

    return render(request, 'planlab/pag_cadernetas.html', {  # Corrija para o caminho correto
        'cadernetas': cadernetas,
        'query': query
    })

@login_required
def home(request):
    planos = Aula.objects.filter(usuario=request.user)  # Assume que você tem um campo 'usuario' nos modelos
    cadernetas = Caderneta.objects.filter(usuario=request.user)
    
    # Dados dinâmicos
    total_aulas = planos.count()  # Corrigido para planos ao invés de aulas
    total_cadernetas = cadernetas.count()  # Contagem de cadernetas
    
    ultimas_aulas = Aula.objects.filter(usuario=request.user).order_by('-data_aula')[:5]
    ultimas_cadernetas = cadernetas.order_by('-data_aula')[:5]  # Alterado para 'data_aula' em vez de 'data_criacao'
    
    contexto = {
        'total_aulas': total_aulas,
        'total_cadernetas': total_cadernetas,
        'ultimas_aulas': ultimas_aulas,
        'ultimas_cadernetas': ultimas_cadernetas,
    }
    return render(request, 'home.html', contexto)




