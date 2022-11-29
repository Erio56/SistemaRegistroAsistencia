from django.db import models
from User.models import Empleado
import datetime
from django.utils import timezone


# Create your models here.

class PermisoEmpleado(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    cedula = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="fk_permiso_empleado")
    descripcion = models.TextField(blank=False, max_length=300)
    fecha_solicitud = models.DateTimeField()
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1,
        default='A'
        )
    @property
    def is_past_due(self):
        resultado = timezone.now() > self.fecha_final
        return resultado

    
class VacacionesEmpleado(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    cedula = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="fk_vacacion_empleado")
    fecha_solicitud = models.DateTimeField()
    estado = models.CharField(        
        unique=False,
        null=False,
        blank=False,
        max_length=1,
        default='A'
        )
    @property
    def is_past_due(self):
        resultado = timezone.now() > self.fecha_final
        return resultado