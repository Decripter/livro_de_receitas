from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chef/', include('chef.urls')), # adicionando o arquivo urls.py do modulo chef a arvore de urls do projeto
    path('client/', include('client.urls')), # adicionando o arquivo urls.py do modulo client a arvore de urls do projeto

]
