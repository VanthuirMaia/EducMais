from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import pag_cadernetas, form_caderneta

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('admin/', admin.site.urls),  # Painel de administração
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('cadastro/', views.cadastro, name='cadastro'),  # Cadastro de usuário
    path('caderneta/', views.caderneta, name='caderneta'),  # Caderneta
    path('plano/', views.plano, name='plano'),  # Página do plano
    path('pag_planos_de_aula/', views.pag_planos_de_aula, name='pag_planos_de_aula'),  # Página de planos de aula
    path('form_aula/', views.form_aula, name='form_aula'),  # Formulário de nova aula
    path('cadernetas/', pag_cadernetas, name='pag_cadernetas'),
    path('caderneta/novo/', form_caderneta, name='form_caderneta'),
]