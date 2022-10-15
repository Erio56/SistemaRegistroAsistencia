from rest_framework import viewsets, permissions, serializers

from .models import Empleado, Dependencia, Cargo
from .serializers import EmpleadoSerializer, CargoSerializer, DependenciaSerializer, UserSerializer

from django.contrib.auth.models import User #TODO



class EmpleadoViewSet(viewsets.ModelViewSet):
   queryset = Empleado.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = EmpleadoSerializer
   
class CargoViewSet(viewsets.ModelViewSet):
   queryset = Cargo.objects.all()
   permission_classes = [permissions.IsAuthenticated]
   serializer_class = CargoSerializer
   
class DependenciaViewSet(viewsets.ModelViewSet):
   queryset = Dependencia.objects.all()
   permission_classes = [permissions.IsAuthenticated]
   serializer_class = DependenciaSerializer
   
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer