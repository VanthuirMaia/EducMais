from django.urls import path
from .views import home, login_view, cadastro, caderneta, form, plano

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('caderneta/', caderneta, name='caderneta'),
    path('form/', form, name='form'),
    path('plano/', plano, name='plano'),
]
