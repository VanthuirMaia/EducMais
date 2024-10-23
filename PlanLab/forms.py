from django import forms
from .models import Aula, Caderneta

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula  # O modelo associado ao formulário
        fields = [
            'disciplina', 
            'data_aula', 
            'turma', 
            'semestre', 
            'titulo', 
            'eventos_extraordinarios', 
            'conteudo_programatico', 
            'metodologia', 
            'recursos_necessarios', 
            'avaliacao_observacoes', 
            'observacoes'
        ]

        # Labels personalizados (opcional)
        labels = {
            'disciplina': 'Disciplina',
            'data_aula': 'Data da Aula',
            'turma': 'Turma',
            'semestre': 'Semestre',
            'titulo': 'Título',
            'eventos_extraordinarios': 'Eventos Extraordinários',
            'conteudo_programatico': 'Conteúdo Programático',
            'metodologia': 'Metodologia',
            'recursos_necessarios': 'Recursos Necessários',
            'avaliacao_observacoes': 'Avaliação/Observações',
            'observacoes': 'Observações'
        }

        # Textos de ajuda (opcional)
        help_texts = {
            'disciplina': 'Informe a disciplina referente à aula.',
            'data_aula': 'Selecione a data em que a aula será realizada.',
            'semestre': 'Digite o semestre correspondente à turma.',
        }

        # Personalização de widgets
        widgets = {
            'data_aula': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Campo de data com o widget HTML5 apropriado
            'conteudo_programatico': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'metodologia': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'recursos_necessarios': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'avaliacao_observacoes': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }


class CadernetaForm(forms.ModelForm):
    class Meta:
        model = Caderneta
        fields = [
            'data_aula',
            'disciplina',
            'serie',
            'semestre',
            'titulo',
            'eventos',
            'conteudo',
            'materiais',
            'atividade',
        ]

        # Labels personalizados (opcional)
        labels = {
            'data_aula': 'Data da Aula',
            'disciplina': 'Disciplina',
            'serie': 'Série',
            'semestre': 'Semestre',
            'titulo': 'Título',
            'eventos': 'Eventos',
            'conteudo': 'Conteúdo',
            'materiais': 'Materiais',
            'atividade': 'Atividade',
        }

        # Textos de ajuda (opcional)
        help_texts = {
            'data_aula': 'Selecione a data da aula.',
            'disciplina': 'Informe a disciplina.',
            'serie': 'Informe a série.',
            'semestre': 'Informe o semestre.',
            'titulo': 'Informe o título da aula.',
            'eventos': 'Descreva os eventos relacionados à aula.',
            'conteudo': 'Descreva o conteúdo abordado na aula.',
            'materiais': 'Liste os materiais utilizados.',
            'atividade': 'Descreva as atividades realizadas.',
        }

        # Personalização de widgets
        widgets = {
            'data_aula': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Campo de data com o widget HTML5 apropriado
            'conteudo': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'materiais': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'eventos': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'atividade': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

class PlanoAula(forms.ModelForm):
    class Meta:
        model = Aula  # Certifique-se de que está usando o modelo correto
        fields = '__all__'  # Isso irá incluir todos os campos do modelo Aula


