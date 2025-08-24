from django.contrib import admin
from conforme_con_cuerpo.models import conforme_con_cuerpo
@admin.register(conforme_con_cuerpo)
class conformeCuerpoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de conforme con cuerpo"
admin.site.site_title = "Gestión de conforme con cuerpo"
admin.site.index_title = "Gestión de conforme con cuerpo"
