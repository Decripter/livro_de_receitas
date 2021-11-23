from receitas.models import Receita
from rest_framework import serializers

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'chef', 'receita']