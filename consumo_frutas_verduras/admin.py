from django.contrib import admin

from consumo_frutas_verduras.models import consumo_frutas_verduras
@admin.register(consumo_frutas_verduras)
class consumoFrutasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de consumo de frutas y verduras"
admin.site.site_title = "Gestión de consumo de frutas y verduras"
admin.site.index_title = "Gestión de consumo de frutas y verduras"
