from django.db import models
from django.contrib.auth.models import User

class Aula(models.Model):
    # Campos do modelo Aula
    disciplina = models.CharField(max_length=100, verbose_name='Disciplina')
    data_aula = models.DateField(verbose_name='Data da Aula')
    turma = models.CharField(max_length=100, verbose_name='Turma')
    semestre = models.IntegerField(verbose_name='Semestre')
    titulo = models.CharField(max_length=200, verbose_name='Título')
    eventos_extraordinarios = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name='Eventos Extraordinários'
    )
    conteudo_programatico = models.TextField(verbose_name='Conteúdo Programático')
    metodologia = models.TextField(verbose_name='Metodologia')
    recursos_necessarios = models.TextField(verbose_name='Recursos Necessários')
    avaliacao_observacoes = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='Avaliação e Observações'
    )
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return f'{self.titulo} - {self.disciplina}'

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['data_aula']  # Ordenar as aulas pela data da aula

class Caderneta(models.Model):
    aluno = models.CharField(max_length=100)
    data_aula = models.DateField()
    disciplina = models.CharField(max_length=100)
    serie = models.CharField(max_length=50)  # Campo para Série/Ano
    semestre = models.CharField(max_length=50)  # Campo para Semestre
    titulo = models.CharField(max_length=100)  # Campo para Título da Aula
    eventos = models.TextField(blank=True, null=True)  # Campo para Eventos Extraordinários
    conteudo = models.TextField()  # Campo para Conteúdo
    materiais = models.TextField(blank=True, null=True)  # Campo para Materiais Utilizados
    atividade = models.TextField(blank=True, null=True)  # Campo para Atividade Prática
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.aluno} - {self.disciplina} ({self.data_aula})'