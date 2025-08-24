import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Personas
@admin.action(description="Exportar a CSV")
def exportar_a_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=personas.csv'
    writer = csv.writer(response)
    writer.writerow(['Nombre Completo', 'Género', 'Edad', 'Peso', 'Estatura', 'IMC', 'Clasificación'])
    for persona in queryset:
        writer.writerow([
            persona.nombre_completo,
            persona.genero,
            persona.edad,
            persona.peso,
            persona.estatura,
            persona.imc,
            persona.clasificacion
        ])
    return response

@admin.register(Personas)
class datosPersonasAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'edad', 'peso', 'estatura', 'imc', 'genero', 'comida_diaria', 'consumo_comida_rapida',
        'consumo_frutas_verduras',
        'consumo_alcohol', 'horas_de_sueno', 'estres_ansiedad', 'conforme_con_cuerpo',
        'actividades_fisicas', 'tipo_de_transporte', 'tiempo_en_pantallas',
        'habitos_alimentarios', 'antecedentes_familiares', 'entorno_social',
        'condiciones_medicas', 'consumo_medicamentos', 'clasificacion', 'created_at']
    actions = [exportar_a_csv]
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()

    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE PERSONAS"
admin.site.site_title = "GESTIÓN DE PERSONAS"
admin.site.index_title = "ADMINISTRACIÓN Y GESTIÓN DE PERSONAS"