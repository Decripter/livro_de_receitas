from rest_framework import viewsets, filters # O pacote filter será responsável por gerenciar a busca
from django_filters.rest_framework import DjangoFilterBackend # Importando pacote responsável gerenciar a filtragem

from receitas.models import ReceitaModel # Importamos o model do módulo receitas
from client.serializers import ReceitaSerializer # Importamos o serializer do módulo client

# Esta classe é apenas de leitura, então só é possível fazer requisições GET, não permitindo que o cliente altere ou delete as receitas
class ReceitasViewSet(viewsets.ReadOnlyModelViewSet):

    """
    Aqui podemos ver todas as receitas criadas.

    Podemos filtrar por chef em filtros, lá tem uma lista dos chefs.

    Podemos realizar uma busca usando o campo de busca.

    Tanto a busca quanto o filtro pode ser feito diretamente através da URL, sendo possível mesclar os dois recurssos ex:

    .../client/?chef=1 > Irá exibir apenas as receitas cadastradas pelo chef '1'.

    .../client/?search=queijo > Irá exibir apenas as receitas que contiverem 'queijo' no texto da receita.

    .../client/?chef=1&search=queijo > Irá exibir apenas as receitas cadastradas pelo chef '1' e apenas aquelas que contiverem 'queijo' no texto da receita

    """
    
    queryset = ReceitaModel.objects.all() # Busca todos os registros e exibe na raiz da página(.../client/)
    serializer_class = ReceitaSerializer  # O serializer é responsável por traduzir objetos do model do Django
                                          # em outros formatos como XML, JSON ..., que podem ser usados nas views.

    
    # DjangoFilterBackend será responsável por filtrar por chef.
    # SearchFilter será responsável por possibilitar a pesquisa nos registros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    
    filterset_fields = ['chef'] # Campo que será filtrado > DjangoFilterBackend.
    search_fields = ['receita'] # Campo onde a pesquisa irá atuar > SearchFilter.