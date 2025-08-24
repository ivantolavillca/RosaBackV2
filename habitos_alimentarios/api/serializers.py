from rest_framework import serializers
from habitos_alimentarios.models import habitos_alimentarios


class HabitosAlimentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = habitos_alimentarios
        fields = ['id', 'nombre']