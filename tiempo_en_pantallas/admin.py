from django.contrib import admin

from tiempo_en_pantallas.models import tiempo_en_pantallas
@admin.register(tiempo_en_pantallas)
class generoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "ADMINISTRACIÓN DE TIEMPO EN PANTALLAS"
admin.site.site_title = "GESTIÓN DE TIEMPO EN PANTALLAS"
admin.site.index_title = "GESTIÓN DE TIEMPO EN PANTALLAS"