from django.contrib import admin

from entorno_social.models import entorno_social
@admin.register(entorno_social)
class entornoSocialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de entorno social"
admin.site.site_title = "Gestión de entorno social"
admin.site.index_title = "Gestión de entorno social"
