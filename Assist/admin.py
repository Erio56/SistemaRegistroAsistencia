from django.contrib import admin
from .models import *


# Register your models here.
class Asistencia_EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields= ('fecha_hora_asitencia',)

admin.site.register(Asistencia_Empleado, Asistencia_EmpleadoAdmin)
admin.site.register(Horario)