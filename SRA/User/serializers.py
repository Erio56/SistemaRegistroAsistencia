from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Empleado, Cargo, Dependencia


class EmpleadoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Empleado
      fields = ('cuenta_usuario', 'cedula', 'nombres', 'apellidos', 'direccion',
                'telefono', 'fecha_nacimiento', 'estado', 'email', 'cargo')
      
class CargoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cargo
      fields = ('id','nombre_cargo', 'dependencia', 'estado')
      
class DependenciaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Dependencia
      fields = ('id','nombre_dependencia')      
      
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']