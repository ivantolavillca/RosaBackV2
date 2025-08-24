from rest_framework import serializers
from actividades_fisicas.api.serializers import ActividadesFisicasSerializer
from antecedentes_familiares.api.serializers import AntecedentesFamiliaresSerializer
from comida_diaria.api.serializers import ComidaDiariaSerializer
from genero.api.serializers import GeneroSerializer
from habitos_alimentarios.api.serializers import HabitosAlimentariosSerializer
from horas_de_sueno.api.serializers import HorasDeSuenoSerializer
from personas.models import Personas
from clasificacion_peso.api.serializers import ClasificacionSerializer
from decimal import Decimal
from django.core.exceptions import ValidationError

from rest_framework import serializers

from tiempo_en_pantallas.api.serializers import TiempoEnPantallasSerializer
from tipo_de_transporte.api.serializers import CTipoDeTransporteSerializer


class PersonaSerializer(serializers.ModelSerializer):
    # genero = GeneroSerializer(read_only=True)
    # comida_diaria = ComidaDiariaSerializer(read_only=True)
    # horas_de_sueno=HorasDeSuenoSerializer(read_only=True)
    # tipo_de_transporte=CTipoDeTransporteSerializer(read_only=True)
    # tiempo_en_pantallas=TiempoEnPantallasSerializer(read_only=True)
    # habitos_alimentarios=HabitosAlimentariosSerializer(read_only=True)
    # clasificacion = ClasificacionSerializer(read_only=True)
    class Meta:
        model = Personas
        fields = [
            'id', 'nombre_completo', 'edad', 'peso', 'estatura', 'imc','genero', 'comida_diaria', 'consumo_comida_rapida', 'consumo_frutas_verduras',
            'consumo_alcohol', 'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
            'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
            'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
            'condiciones_medicas', 'consumo_medicamentos', 'clasificacion','perimetro_cintura', 'perimetro_cadera'
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.genero:
            rep['genero'] = {
                'id': instance.genero.id,
                'nombre': instance.genero.nombre
            }
        if instance.comida_diaria:
            rep['comida_diaria'] = {
                'id': instance.comida_diaria.id,
                'nombre': instance.comida_diaria.nombre
            }
        if instance.horas_de_sueno:
            rep['horas_de_sueno'] = {
                'id': instance.horas_de_sueno.id,
                'nombre': instance.horas_de_sueno.nombre
            }
        if instance.tipo_de_transporte:
            rep['tipo_de_transporte'] = {
                'id': instance.tipo_de_transporte.id,
                'nombre': instance.tipo_de_transporte.nombre
            }
        if instance.tiempo_en_pantallas:
            rep['tiempo_en_pantallas'] = {
                'id': instance.tiempo_en_pantallas.id,
                'nombre': instance.tiempo_en_pantallas.nombre
            }
        if instance.habitos_alimentarios:
            rep['habitos_alimentarios'] = {
                'id': instance.habitos_alimentarios.id,
                'nombre': instance.habitos_alimentarios.nombre
            }
        if instance.clasificacion:
            rep['clasificacion'] = {
                'id': instance.clasificacion.id,
                'nombre': instance.clasificacion.nombre
            }
        return rep
    def validate_edad(self, value):
        if value < 13 or value > 18:
            raise ValidationError("La edad debe estar entre 13 y 18 años.")
        return value

    def validate_peso(self, value):
        if not isinstance(value, Decimal):
            raise ValidationError("El peso debe ser un número decimal.")
        if value <= 0:
            raise ValidationError("El peso debe ser un valor positivo.")
        return value

    def validate_estatura(self, value):
        if not isinstance(value, Decimal):
            raise ValidationError("La estatura debe ser un número decimal.")
        if value <= 0:
            raise ValidationError("La estatura debe ser un valor positivo.")
        return value

class ReportPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = [
            'id', 'nombre_completo', 'edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria',
            'consumo_comida_rapida', 'consumo_frutas_verduras',
            'consumo_alcohol', 'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
            'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
            'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
            'condiciones_medicas', 'consumo_medicamentos', 'clasificacion','perimetro_cintura', 'perimetro_cadera'
        ]
class ModeloDatos(serializers.Serializer):
    edad = serializers.FloatField()
    peso = serializers.FloatField()
    estatura = serializers.FloatField()
    genero = serializers.FloatField()
    comida_diaria = serializers.FloatField()
    consumo_comida_rapida = serializers.BooleanField()
    consumo_frutas_verduras = serializers.BooleanField()
    consumo_alcohol = serializers.BooleanField()
    horas_de_sueno = serializers.FloatField()
    estres_ansiedad = serializers.BooleanField()
    conforme_con_cuerpo = serializers.BooleanField()
    actividades_fisicas = serializers.BooleanField()
    tipo_de_transporte = serializers.FloatField()
    tiempo_en_pantallas = serializers.FloatField()
    habitos_alimentarios = serializers.FloatField()
    antecedentes_familiares = serializers.BooleanField()
    entorno_social = serializers.BooleanField()
    condiciones_medicas = serializers.BooleanField()
    consumo_medicamentos = serializers.BooleanField()
    perimetro_cintura = serializers.FloatField()
    perimetro_cadera = serializers.FloatField()