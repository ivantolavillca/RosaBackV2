from django.contrib import admin

from tipo_de_transporte.models import tipo_de_transporte
@admin.register(tipo_de_transporte)
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
admin.site.site_header = "ADMINISTRACIÓN DE TIPO DE TRANSPORTE"
admin.site.site_title = "GESTIÓN DE TIPO DE TRANSPORTE"
admin.site.index_title = "GESTIÓN DE TIPO DE TRANSPORTE"
