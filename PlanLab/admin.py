from django.contrib import admin
from .models import Aula, Disciplina, Turma, Semestre

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'data_aula', 'usuario')
    search_fields = ('titulo', 'disciplina', 'usuario__username')
    list_filter = ('disciplina', 'semestre')


admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Semestre)