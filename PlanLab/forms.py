from django import forms
from .models import Aula, Caderneta, Profile

from django import forms
from .models import Aula, Disciplina, Turma, Semestre

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
            'titulo': 'Informe o título da aula.',
            'eventos_extraordinarios': 'Descreva eventos extraordinários (se houver).',
            'conteudo_programatico': 'Informe o conteúdo programático da aula.',
            'metodologia': 'Descreva a metodologia utilizada na aula.',
            'recursos_necessarios': 'Liste os recursos necessários para a aula.',
            'avaliacao_observacoes': 'Comentários sobre a avaliação da aula.',
            'observacoes': 'Observações gerais sobre a aula.',
        }

        # Personalização de widgets
        widgets = {
            'data_aula': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Campo de data com o widget HTML5 apropriado
            'conteudo_programatico': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'metodologia': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'recursos_necessarios': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'avaliacao_observacoes': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'eventos_extraordinarios': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    # Personalização dos campos relacionados a outros modelos
    disciplina = forms.ModelChoiceField(queryset=Disciplina.objects.all(), empty_label="Selecione a disciplina", required=True)
    turma = forms.ModelChoiceField(queryset=Turma.objects.all(), empty_label="Selecione a turma", required=True)
    semestre = forms.ModelChoiceField(queryset=Semestre.objects.all(), empty_label="Selecione o semestre", required=True)



class CadernetaForm(forms.ModelForm):
    class Meta:
        model = Caderneta
        fields = [
            'data_aula',
            'disciplina',
            'turma',
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
            'turma': 'Turma',
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
            'turma': 'Informe a turma.',
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']