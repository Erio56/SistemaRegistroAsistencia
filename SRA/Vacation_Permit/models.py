from django.db import models
from User.models import Empleado
# Create your models here.

class PermisoEmpleado(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    cedula = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="fk_permiso_empleado")
    descripcion = models.TextField(blank=False, max_length=300)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1,
        default='A'
        )
    
class VacacionesEmpleado(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    cedula = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="fk_vacacion_empleado")
    estado = models.CharField(        
        unique=False,
        null=False,
        blank=False,
        max_length=1,
        default='A'
        )