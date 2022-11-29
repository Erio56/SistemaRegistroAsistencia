from django.forms import ModelForm, fields
from django import forms
from .models import Asistencia_Empleado, Horario

class createAsistenciaForm(forms.ModelForm):
    class Meta:
            model = Asistencia_Empleado
            fields = ['observacion']
            widgets = {
                'observacion': forms.TextInput(attrs={
                    'required': False
                })
            }
            