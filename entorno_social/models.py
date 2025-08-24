from django.db import models

class entorno_social(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Tiene entorno social con obesidad amistades, companeros con los que frecuenta?")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "ENTORNO SOCIAL"
        verbose_name_plural = "ENTORNO SOCIAL"
