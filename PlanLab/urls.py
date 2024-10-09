from django.urls import path
from .views import home, login_view, cadastro, caderneta, form, plano, planos_de_aula, pag_cadernetas

urlpatterns = [
    path('', home, name='home'),               # URL para a página inicial
    path('login/', login_view, name='login'),  # URL para a página de login
    path('cadastro/', cadastro, name='cadastro'),
    path('caderneta/', caderneta, name='caderneta'),
    path('form/', form, name='form'),
    path('plano/', plano, name='plano'),       # URL para a funcionalidade "plano"
    path('planos_de_aula/', planos_de_aula, name='planos_de_aula'),  # URL para a página "Planos de Aula"
    path('pag_cadernetas/', pag_cadernetas, name='pag_cadernetas'),  # URL para a página "Planos de Aula"

]
