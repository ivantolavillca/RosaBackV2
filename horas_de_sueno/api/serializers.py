from rest_framework import serializers
from horas_de_sueno.models import horas_de_sueno


class HorasDeSuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = horas_de_sueno
        fields = ['id', 'nombre']