from django.db import models

class horas_de_sueno(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Horas de sueño por noche")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Horas de sueño por noche"
        verbose_name_plural = "Horas de sueño por noche"
