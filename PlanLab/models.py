from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

class Aula(models.Model):
    disciplina = models.CharField(max_length=100)
    data_aula = models.DateField()
    turma = models.CharField(max_length=100)
    semestre = models.CharField(max_length=10)
    titulo = models.CharField(max_length=200)
    conteudo_programatico = models.TextField()
    metodologia = models.TextField()
    recursos_necessarios = models.TextField()
    avaliacao_observacoes = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    eventos_extraordinarios = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo