from django.contrib import admin
from consumo_alcohol.models import consumo_alcohol
@admin.register(consumo_alcohol)
class consumoAlcoholAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de consumo de alcohol"
admin.site.site_title = "Gestión de consumo de alcohol"
admin.site.index_title = "Gestión de consumo de alcohol"
