from django.db import models
class Clasificacion(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre de la clasificación")
    imc_min= models.FloatField(verbose_name="IMC mínimo", default=0)
    imc_max= models.FloatField(verbose_name="IMC máximo",default=0)
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Clasificación de peso"
        verbose_name_plural = "Clasificaciones de peso"
