from django.contrib import admin

from planes_recomendaciones.models import RecomendacionesModel


# Register your models here.
@admin.register(RecomendacionesModel)
class recomendacionesAdmin(admin.ModelAdmin):
    list_display = ['recomendaciones', 'clasificacion', 'tipo']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()

    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "RECOMENDACIONES Y PLANES"
admin.site.site_title = "RECOMENDACIONES Y PLANES"
admin.site.index_title = "RECOMENDACIONES Y PLANES"