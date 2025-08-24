from rest_framework import serializers
from conforme_con_cuerpo.models import conforme_con_cuerpo


class ConformeConCuerpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = conforme_con_cuerpo
        fields = ['id', 'nombre']