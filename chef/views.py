from rest_framework import viewsets

from .serializers import ReceitaSerializer # Importamos o serializer do módulo chef 
from receitas.models import ReceitaModel # Importamos o model do módulo receitas

# Esta classe irá gerenciar todas as requisiões que iremos precisar(GET, POST, PUT e DELETE)
class ReceitasViewSet(viewsets.ModelViewSet):
    """
    Retorna uma lista com todas as receitas cadastradas.

    É possível acrescentar novas receitas preenchendo o formulário abaixo.

    Para editar uma receita coloque o 'id' na URL(/chef/1/), isto vai te direcionar para uma página de
    detalhes onde será possível editar ou excluir a receita.
    
    """
    queryset = ReceitaModel.objects.all() # Busca todos os registros e exibe na raiz da página(.../chef/)
    serializer_class = ReceitaSerializer  # O serializer é responsável por traduzir objetos do model do Django
                                          # em outros formatos como XML, JSON ..., que podem ser usados nas views.



    