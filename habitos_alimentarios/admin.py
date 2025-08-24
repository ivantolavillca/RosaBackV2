from django.contrib import admin

from habitos_alimentarios.models import habitos_alimentarios
@admin.register(habitos_alimentarios)
class habitosAlimenticiosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
    def delete_model(self, request, obj):
        obj.is_delete = True
        obj.save()
    def delete_queryset(self, request, queryset):
        queryset.update(is_delete=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_delete=False)
admin.site.site_header = "Administración de hábitos alimentarios"
admin.site.site_title = "Gestión de hábitos alimentarios"
admin.site.index_title = "Gestión de hábitos alimentarios"
