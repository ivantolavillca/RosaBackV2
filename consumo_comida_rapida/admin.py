from django.contrib import admin
from consumo_comida_rapida.models import consumo_comida_rapida
@admin.register(consumo_comida_rapida)
class consumoComidaRapidaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de consumo de comida rápida"
admin.site.site_title = "Consumo de comida rápida"
admin.site.index_title = "Gestión de consumo de comida rápida"