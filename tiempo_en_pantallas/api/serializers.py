from rest_framework import serializers
from tiempo_en_pantallas.models import tiempo_en_pantallas



class TiempoEnPantallasSerializer(serializers.ModelSerializer):
    class Meta:
        model = tiempo_en_pantallas
        fields = ['id', 'nombre']