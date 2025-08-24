from django.db import models
class tiempo_en_pantallas(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Cuantas horas al día pasas frente a las pantallas (TV, videojuegos, celular)")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Tiempo frente a las pantallas  (TV, videojuegos, celular) por día"
        verbose_name_plural = "Tiempo frente a las pantallas  (TV, videojuegos, celular) por día"
