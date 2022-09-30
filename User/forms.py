from django.forms import ModelForm, fields
from django import forms
from .models import Cargo, Dependencia, Empleado


# class linkEmpleadoCargoForm(ModelForm):
#     class Meta:
#         model = Empleado
#         fields = ['cedula_empleado','cargo']

class createCargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre_cargo','dependencia']
        
class linkEmpleadoForm(forms.Form):
    nombres = forms.CharField(label='Nombre', max_length=45, required=True)
    cedula = forms.CharField(label='Cedula', max_length=15, required=True)
    apellidos = forms.CharField(label='Apellidos', max_length=45, required=True)
    direccion = forms.CharField(label='Dirección', max_length=45, required=True)
    telefono = forms.CharField(label='Teléfono', max_length=20, required=True)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(
        format=('%D-%M-%Y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Selecciona una fecha',
               'type': 'date'
              }))