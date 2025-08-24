from django.db import models
class habitos_alimentarios(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="cocinan en casa o comen fuera frecuentemente?")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Hábitos alimentarios del hogar"
        verbose_name_plural = "Hábitos alimentarios del hogar"