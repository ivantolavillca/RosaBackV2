from django.db import models

class conforme_con_cuerpo(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="¿Te sientes conforme con tu cuerpo o peso?")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "CONFORME CON EL CUERPO"
        verbose_name_plural = "¿Te sientes conforme con tu cuerpo o peso?"