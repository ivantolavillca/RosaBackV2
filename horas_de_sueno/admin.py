from django.contrib import admin

from horas_de_sueno.models import horas_de_sueno
@admin.register(horas_de_sueno)
class horasSuenoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de horas de sueño"
admin.site.site_title = "Gestión de horas de sueño"
admin.site.index_title = "Gestión de horas de sueño"

