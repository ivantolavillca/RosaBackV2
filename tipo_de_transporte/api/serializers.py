from rest_framework import serializers
from consumo_alcohol.models import consumo_alcohol
from tipo_de_transporte.models import tipo_de_transporte


class CTipoDeTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_de_transporte
        fields = ['id', 'nombre']