from rest_framework import serializers
from consumo_alcohol.models import consumo_alcohol


class ConsumoBebidasAlcoholicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumo_alcohol
        fields = ['id', 'nombre']