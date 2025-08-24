from django.contrib import admin
from clasificacion_peso.models import Clasificacion
@admin.register(Clasificacion)
class ClasificacionPesoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de clasificación de peso"
admin.site.site_title = "Clasificación de peso"
admin.site.index_title = "Gestión de clasificación de peso"