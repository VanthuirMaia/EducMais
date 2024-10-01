from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.models.CharField(max_length=100)

