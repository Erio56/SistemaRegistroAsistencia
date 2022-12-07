from django.forms import ModelForm, fields
from django import forms
from .models import Asistencia_Empleado, Horario, Hora

class createAsistenciaForm(forms.ModelForm):
    class Meta:
            model = Asistencia_Empleado
            fields = ['observacion']
            widgets = {
                'observacion': forms.TextInput(attrs={
                    'required': False
                })
            }
        
class createHoraForm(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['hora_entrada','hora_salida']
        widgets = {
            'hora_entrada': forms.TimeInput(attrs={
                'type': 'Time',
                'class': 'input',
                'required': False
            }),
            'hora_salida':  forms.TimeInput(attrs={
                'type': 'Time',
                'class': 'input',
                'required': False
            })
        }