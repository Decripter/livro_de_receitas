from receitas.models import ReceitaModel
from django.shortcuts import redirect
from django.urls import reverse

from chef.serializers import ReceitaSerializer
from rest_framework import viewsets, permissions

class ReceitasViewSet(viewsets.ModelViewSet):

    queryset = ReceitaModel.objects.all()
    serializer_class = ReceitaSerializer


    