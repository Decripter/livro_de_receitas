from receitas.models import ReceitaModel
from django.shortcuts import redirect
from django.urls import reverse

from chef.serializers import ReceitaSerializer
from rest_framework import viewsets, permissions

class ReceitasViewSet(viewsets.ModelViewSet):
    """
    Retorna uma lista com todas as receitas cadastradas.

    É possível acrescentar novas receitas preenchendo o formulário abaixo.

    Para editar uma receita coloque o 'id' na URL(/chef/1), isto vai te direcionar ppara uma página de
    detalhes onde será possível editar ou excluir a receita.
    
    """
    queryset = ReceitaModel.objects.all()
    serializer_class = ReceitaSerializer



    