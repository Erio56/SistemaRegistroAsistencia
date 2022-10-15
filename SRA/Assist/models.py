from django.db import models
from User.models import Empleado
# Create your models here.

class Asistencia_Empleado(models.Model):
    cedula = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="fk_asistencia_cedula")
    fecha_hora_asitencia = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=True,
        max_length=45)
    def __str__(self):
        return self.observacion

class Horario(models.Model):
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    fecha = models.DateField()
    observacion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1,
        default='A'
        )