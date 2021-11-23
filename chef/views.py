from receitas.models import Receita
from django.shortcuts import redirect
from django.urls import reverse

from chef.serializers import ReceitaSerializer
from rest_framework import viewsets, permissions

class ReceitasViewSet(viewsets.ModelViewSet):

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


    