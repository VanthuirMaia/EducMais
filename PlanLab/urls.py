from django.urls import path
from .views import login_view, index, planos_de_aula, pagina_aula, editar_plano, formulario, excluir_plano

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', index, name='index'),
    path('planos_de_aula/', planos_de_aula, name='planos_de_aula'),
    path('pagina_aula/<int:plano_id>/', pagina_aula, name='pagina_aula'),
    path('editar_plano/<int:plano_id>/', editar_plano, name='editar_plano'),
    path('formulario/', formulario, name='formulario'),
    path('excluir_plano/<int:plano_id>/', excluir_plano, name='excluir_plano'),
]