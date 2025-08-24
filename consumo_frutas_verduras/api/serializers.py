from rest_framework import serializers
from consumo_frutas_verduras.models import consumo_frutas_verduras

class ConsumoFrutasVerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumo_frutas_verduras
        fields = ['id', 'nombre']
        