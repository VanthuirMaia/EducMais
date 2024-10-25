from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('caderneta/', views.caderneta, name='caderneta'),  # Caderneta
    path('plano/<int:id>/', views.plano, name='plano'),  # Página do plano com ID
    path('pag_planos_de_aula/', views.pag_planos_de_aula, name='pag_planos_de_aula'),  # Página de planos de aula
    path('form_aula/', views.form_aula, name='form_aula'),  # Formulário de nova aula
    path('plano/<int:plano_id>/editar/', views.form_editar_aula, name='form_editar_aula'),
    path('cadernetas/', views.pag_cadernetas, name='pag_cadernetas'),
    path('caderneta/novo/', views.form_caderneta, name='form_caderneta'),
]

