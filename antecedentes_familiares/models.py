from django.db import models

class antecedentes_familiares(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Tiene antecedentes familiares de obesidad?")
    is_delete= models.BooleanField(default=False, verbose_name="Eliminado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Antecedente familiar"
        verbose_name_plural = "¿Tiene antecedentes familiares de obesidad?"