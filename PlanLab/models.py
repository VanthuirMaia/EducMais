from django.db import models
from django.contrib.auth.models import User

# Modelo para representar uma disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Modelo para representar uma turma
class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Modelo para representar um semestre
class Semestre(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


# Modelo para representar uma aula
class Aula(models.Model):
    # Relacionamentos
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    # Campos principais
    data_aula = models.DateField(verbose_name='Data da Aula')
    titulo = models.CharField(max_length=200, verbose_name='Título')
    eventos_extraordinarios = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Eventos Extraordinários'
    )
    conteudo_programatico = models.TextField(verbose_name='Conteúdo Programático')
    metodologia = models.TextField(verbose_name='Metodologia')
    recursos_necessarios = models.TextField(verbose_name='Recursos Necessários')
    avaliacao_observacoes = models.TextField(
        blank=True, null=True, verbose_name='Avaliação e Observações'
    )
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    
    # Configurações do modelo
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['data_aula']  # Ordenar as aulas pela data da aula

    def __str__(self):
        return f'{self.titulo} - {self.disciplina}'


# Modelo para representar uma caderneta de aula
class Caderneta(models.Model):
    # Relacionamentos
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    # Campos principais
    data_aula = models.DateField(verbose_name='Data da Aula')
    titulo = models.CharField(max_length=200, verbose_name='Título')
    eventos = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Eventos'
    )
    conteudo = models.TextField(verbose_name='Conteúdo')
    materiais = models.TextField(blank=True, null=True, verbose_name='Materiais')
    atividade = models.TextField(blank=True, null=True, verbose_name='Atividade')

    # Configurações do modelo
    class Meta:
        verbose_name = 'Caderneta'
        verbose_name_plural = 'Cadernetas'
        ordering = ['data_aula']  # Ordenar as cadernetas pela data da aula

    def __str__(self):
        return f'{self.titulo} - {self.disciplina}'
