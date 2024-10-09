from django.contrib import admin
from django.urls import path, include  # Importando include

urlpatterns = [
    path('admin/', admin.site.urls),           # URL para o admin
    path('', include('PlanLab.urls')),         # Incluindo as URLs da aplicação PlanLab
]
