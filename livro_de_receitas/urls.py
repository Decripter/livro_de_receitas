from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('receitas/', include('receitas.urls')) # adicionando o arquivo urls.py do modulo receitas a arvore de urls do projeto
]
