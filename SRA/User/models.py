from django.db import models
from django.conf import settings
# Create your models here.

class Dependencia(models.Model):
    nombre_dependencia = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1
        )
    def __str__(self):
        return self.nombre_dependencia
    
class Cargo(models.Model):
    nombre_cargo = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45)
    dependencia =  models.ForeignKey(Dependencia, on_delete=models.CASCADE, related_name='fk_dependencia')
    estado = models.CharField(        
        unique=False, 
        null=False,
        blank=False,
        max_length=1,
        )
    def __str__(self):
        return self.nombre_cargo
    
class Empleado(models.Model):
    cuenta_usuario= models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        )
    
    cedula = models.CharField(
        primary_key=True,
        unique=True, 
        null=False,
        blank=False,
        max_length=15
    )
    nombres =  models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    apellidos = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    direccion = models.CharField(
        unique=False, 
        null=False,
        blank=False,
        max_length=45
    )
    telefono = models.CharField(
        unique=False, 
        null=False,
        max_length=45
    )
    fecha_nacimiento = models.DateField()
    email =  models.EmailField()
    cargo = models.ForeignKey(Cargo, null=True, blank=True, related_name='fk_dependencia', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombres + ' ' + self.apellidos