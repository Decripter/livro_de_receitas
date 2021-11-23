from receitas.models import ReceitaModel
from rest_framework import serializers

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaModel
        fields = ['id', 'chef', 'receita']