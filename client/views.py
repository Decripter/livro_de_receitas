from receitas.models import ReceitaModel

from client.serializers import ReceitaSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class ReceitasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReceitaModel.objects.all()
    serializer_class = ReceitaSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['chef']
    search_fields = ['receita']