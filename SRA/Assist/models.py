from django.db import models
from User.models import Empleado
from django.utils import timezone
# Create your models here.
import datetime


class Asistencia_Empleado(models.Model):
    cedula = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, related_name="fk_asistencia_cedula")
    fecha_hora_asitencia = models.DateTimeField(auto_now_add=True)
    llegaTarde = models.BooleanField(default=False)
    falta = models.BooleanField(default=False)
    observacion = models.CharField(
        unique=False, 
        null=True,
        blank=True,
        max_length=45)
    def __str__(self):
        return self.observacion
    
    
class Hora(models.Model):
    hora_entrada = models.TimeField(
        default = None,
        null = True,
        blank = False
        )
    hora_salida = models.TimeField(
        default = None,
        null = True,
        blank = False
        )

class Horario(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="fk_horario_empleado")
    lunes = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_lunes", null = True, default=None)
    martes = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_martes", null = True, default=None)
    miercoles = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_miercoles", null = True, default=None)
    jueves = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_jueves", null = True, default=None)
    viernes = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_viernes", null = True, default=None)
    sabado = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_sabado", null = True, default=None)
    domingo = models.ForeignKey(Hora, on_delete=models.CASCADE, related_name="fk_hora_domingo", null = True, default=None)
    
    @property
    def needsToAssistToday(self):
        now = datetime.datetime.now()
        day = now.strftime("%A")
        match day:
            case 'Monday':
                return self.lunes
            case 'Tuesday':
                return self.martes
            case 'Wednesday':
                return self.miercoles
            case 'Thursday':
                return self.jueves
            case 'Friday':
                return self.viernes
            case 'Saturday':
                return self.sabado
            case 'Sunday':
                return self.domingo
            case _:
                return None
    
