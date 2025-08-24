from rest_framework import serializers
from entorno_social.models import entorno_social


class EntornoSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = entorno_social
        fields = ['id', 'nombre']