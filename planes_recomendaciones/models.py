from django.db import models
from clasificacion_peso.models import Clasificacion
TIPO_CHOICES = [
    ("Terapéutico", "Terapéutico"),
    ("Preventivo", "Preventivo"),
]

class RecomendacionesModel(models.Model):
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE , verbose_name="Clasificación de peso")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de plan")
    recomendaciones = models.TextField( verbose_name="Recomendación o plan")
    is_delete = models.BooleanField(default=False, verbose_name="Eliminado")
    def __str__(self):
        return self.recomendaciones

    class Meta:
        verbose_name = "Recomendaciones o planes"
        verbose_name_plural = "Recomendaciones o planes"
