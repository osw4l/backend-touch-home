from django.contrib import admin
from . import models
# Register your models here.


admin.site.site_header = 'Touch Home Admin'
admin.site.site_title = 'Touch Home Admin'
admin.site.index_title = 'Touch Home Admin'


@admin.register(models.Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'cover']


@admin.register(models.Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_completo', 'telefono', 'correo', 'profesion']