from rest_framework import serializers

from receitas.models import ReceitaModel

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaModel # Nós estamos utilizando o model do módulo receitas
        fields = ['id', 'chef', 'receita'] # Campos do model que iremos utilizar