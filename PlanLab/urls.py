from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),



    path('plano/<int:id>/', views.plano, name='plano'),  # Página do plano com ID
    path('pag_planos_de_aula/', views.pag_planos_de_aula, name='pag_planos_de_aula'),  # Página de planos de aula
    path('form_aula/', views.form_aula, name='form_aula'),  # Formulário de nova aula
    path('plano/<int:plano_id>/editar/', views.form_editar_aula, name='form_editar_aula'),
    path('plano/<int:plano_id>/excluir/', views.excluir_plano, name='excluir_plano'),
    path('copiar_plano/<int:id>/', views.copiar_plano, name='copiar_plano'),



    path('caderneta/<int:id>/', views.caderneta, name='caderneta'),  # Caderneta
    path('pag_cadernetas/', views.pag_cadernetas, name='pag_cadernetas'),
    path('form_caderneta/', views.form_caderneta, name='form_caderneta'),
    path('caderneta/<int:caderneta_id>/editar/', views.form_editar_caderneta, name='form_editar_caderneta'),
    path('caderneta/excluir/<int:id>/', views.excluir_caderneta, name='excluir_caderneta'),
    path('copiar_caderneta/<int:id>/', views.copiar_caderneta, name='copiar_caderneta'),



]

