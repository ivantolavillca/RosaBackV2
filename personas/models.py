from django.db import models
from clasificacion_peso.models import Clasificacion
from antecedentes_familiares.models import antecedentes_familiares
from condiciones_medicas.models import condiciones_medicas
from consumo_medicamentos.models import consumo_medicamentos
from estres_ansiedad.models import estres_ansiedad
from actividades_fisicas.models import ActividadesFisicas
from comida_diaria.models import comida_diaria
from conforme_con_cuerpo.models import conforme_con_cuerpo
from consumo_alcohol.models import consumo_alcohol
from consumo_frutas_verduras.models import consumo_frutas_verduras
from entorno_social.models import entorno_social
from habitos_alimentarios.models import habitos_alimentarios
from horas_de_sueno.models import horas_de_sueno
from tiempo_en_pantallas.models import tiempo_en_pantallas
from tipo_de_transporte.models import tipo_de_transporte
from genero.models import genero
from consumo_comida_rapida.models import consumo_comida_rapida
from django.db.models import CASCADE
from django.core.exceptions import ValidationError
class Personas(models.Model):
    nombre_completo = models.CharField(max_length=255, verbose_name="Nombre completo")
    #DATOS DE IDENTIFICACION BASICA
    genero = models.ForeignKey(genero, on_delete=models.CASCADE,default=1, verbose_name="Género")
    edad = models.IntegerField( verbose_name="Edad")
    #MEDICION CORPORAL
    peso = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso")
    estatura = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Estatura")
    imc = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="IMC", null=True, blank=True)
    perimetro_cintura =models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Perímetro de cintura",default=0.0)
    perimetro_cadera = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Perímetro de cadera", default=0.0)
    #ESTILO DE VIDA
    comida_diaria = models.ForeignKey(comida_diaria, on_delete=models.CASCADE, verbose_name="¿Cuántas veces comes al dia?")
    consumo_comida_rapida = models.BooleanField(default=False, verbose_name="¿Consumes comida rapida?")
    consumo_frutas_verduras = models.BooleanField(default=False, verbose_name="¿Consumes frutas y verduras?")
    consumo_alcohol = models.BooleanField(default=False,  verbose_name="¿Consúmes bebidas alcoholicas?")
    #SUEÑO Y SALUD MENTAL
    horas_de_sueno = models.ForeignKey(horas_de_sueno, on_delete=models.CASCADE,default=1, verbose_name="¿Cuántas horas descansas por la noche?")
    estres_ansiedad = models.BooleanField(default=False,verbose_name="¿Súfres de estrés o ansiedad?")
    conforme_con_cuerpo = models.BooleanField(default=False, verbose_name="¿Te siéntes conforme con tu cuerpo o peso?")
    #ACTIVIDAD FISICA
    actividades_fisicas = models.BooleanField(default=False, verbose_name="¿Realízas Actividades fisicas?")
    tipo_de_transporte = models.ForeignKey(tipo_de_transporte, on_delete=models.CASCADE,default=1, verbose_name="¿Caminas al colegio o  te transportas en vehiculo?")
    tiempo_en_pantallas = models.ForeignKey(tiempo_en_pantallas, on_delete=models.CASCADE,default=1, verbose_name="¿Cuánto tiempo pasas frente a las pantallas (TV, videojuegos, celular)?")
    #FACTORES CLINICOS
    habitos_alimentarios = models.ForeignKey(habitos_alimentarios, on_delete=models.CASCADE,default=1, verbose_name="¿Comes en casa o fuera frecuentemente?")
    antecedentes_familiares = models.BooleanField(default=False, verbose_name="¿Tienes antecedentes familiares de obesidad en tu familia?")
    entorno_social = models.BooleanField(default=False,  verbose_name="¿Tienes entorno social con obesidad (amistades, compañeros, o con los que frecuenta)?")
    condiciones_medicas = models.BooleanField(default=False,  verbose_name="¿Tienes condiciones medicas como: diabetes tipo 2, presion arterial o colesterol alto?")
    consumo_medicamentos = models.BooleanField(default=False, verbose_name="¿Consumes medicamentos que puedan alterar el peso?")
    #ESTADO DE PESO
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE,default=1,verbose_name="Clasificación de peso")
    #EXTRAS
    is_delete = models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    #VALIDACIONES
    def clean(self):
        if self.edad is None or not (13 <= self.edad <= 18):
            raise ValidationError("La edad debe estar entre 13 y 18 años.")
        if self.peso is None or self.peso <= 0:
            raise ValidationError("El peso debe ser un número positivo.")
        if self.estatura is None or self.estatura <= 0:
            raise ValidationError("La estatura debe ser un número positivo.")

    def save(self, *args, **kwargs):
        if self.peso and self.estatura:
            self.imc = round(float(self.peso) / (float(self.estatura) ** 2), 1)
            if self.imc < 18.5:
                self.clasificacion_id = 1
            elif 18.5 <= self.imc <= 24.9:
                self.clasificacion_id = 2
            elif 25.0 <= self.imc <= 29.9:
                self.clasificacion_id = 3
            elif 30.0 <= self.imc <= 34.9:
                self.clasificacion_id = 4
            elif 35.0 <= self.imc <= 39.9:
                self.clasificacion_id = 5
            else:
                self.clasificacion_id = 6
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_completo
    class Meta:
        verbose_name = "DATOS DE PERSONAS"
        verbose_name_plural = "DATOS DE PERSONAS"

