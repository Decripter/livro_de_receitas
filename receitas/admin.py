from django.contrib import admin

from .models import ChefModel, ReceitaModel # Importando os models

admin.site.register(ChefModel) # Registrando o model ChefModel para ser visível no painel administrativo
admin.site.register(ReceitaModel) # Registrando o model ClientModel para ser visível no painel administrativo

