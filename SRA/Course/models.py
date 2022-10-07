from django.db import models
from User.models import Empleado
# Create your models here.

class Materia(models.Model):
    codigo_materia = models.CharField(
        primary_key=True,   
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    nombre_materia = models.CharField(
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

class Curso(models.Model):
    semestre = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10)
    sede = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10)
    codigo_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='fk_materia')
    cedula_docente = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='fk_docente')
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    salon = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=10)
    estado = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=1,
        default='A'
        )