from receitas.models import ReceitaModel

from client.serializers import ReceitaSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class ReceitasViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Aqui podemos ver todas as receitas criadas.

    Podemos filtrar por chef em filtros, lá tem uma lista dos chefs.

    Podemos realizar uma busca usando o campo de busca.
    
    """
    
    queryset = ReceitaModel.objects.all()
    serializer_class = ReceitaSerializer 
    
    # DjangoFilterBackend será responsável por filtrar por chef.
    # SearchFilter será responsável por possibilitar a pesquisa nos registros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    
    filterset_fields = ['chef'] # Campo que será filtrado > DjangoFilterBackend.
    search_fields = ['receita'] # Campo onde a pesquisa irá atuar > SearchFilter.