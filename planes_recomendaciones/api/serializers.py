from rest_framework import serializers

from planes_recomendaciones.models import RecomendacionesModel


class RecomendacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecomendacionesModel
        fields = ['id', 'recomendaciones', 'clasificacion', 'tipo']