from tkinter import Widget
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
        fields = ['nombre_cargo', 'dependencia']
        
        
        
class createDependenciaForm(ModelForm):
    class Meta:
        model = Dependencia
        fields = ['nombre_dependencia']


class linkEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'cedula', 'apellidos', 'direccion', 'telefono', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                format=('%D-%M-%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona una fecha',
                    'type': 'date'
                    }
                )
            }
