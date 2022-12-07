from SRA.User.models import Empleado
from SRA.Assist.models import Asistencia_Empleado, Horario

def poner_faltas():
   empleados = Empleado.objects.all()
   for Empleado in empleados.iterator():
      asistencia = Asistencia_Empleado(cedula=empleados, falta=True, observacion="")
      asistencia.save()