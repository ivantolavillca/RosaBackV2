from django.contrib import admin

from perimetro_cadera.models import perimetro_cadera
@admin.register(perimetro_cadera)
class perimetroCaderaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de perímetro de cadera"
admin.site.site_title = "Gestión de perímetro de cadera"
admin.site.index_title = "Gestión de perímetro de cadera"