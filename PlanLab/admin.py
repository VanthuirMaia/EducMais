from django.contrib import admin
from .models import Aula, Caderneta, Disciplina, Turma, Semestre

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'data_aula', 'usuario')
    search_fields = ('titulo', 'disciplina', 'usuario__username')
    list_filter = ('disciplina', 'semestre')

# admin.py

@admin.register(Caderneta)
class CadernetaAdmin(admin.ModelAdmin):
    list_display = ('semestre', 'turma', 'disciplina')  # Outros campos aqui...
    search_fields = ('semestre__nome', 'turma__nome', 'disciplina__nome')  # Para facilitar buscas



admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Semestre)