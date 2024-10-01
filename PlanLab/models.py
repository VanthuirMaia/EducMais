from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.models.CharField(max_length=100)

class Aula(models.Model):
    data_aula = models.DateField()
    turma = models.CharField(max_length=100)
    semestre = models.CharField(max_length=10)
    titulo = models.CharField(max_length=200)
    conteudo_programatico = models.TextField()
    metodologia = models.TextField()
    recursos_necessarios = models.TextField()
    avaliacao_observacoes = models.TextField()
    observacoes = models.TextField()
    eventos_extraordinarios = models.TextField()
    uuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)