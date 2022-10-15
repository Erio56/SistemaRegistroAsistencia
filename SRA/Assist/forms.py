from django.forms import ModelForm, fields
from django import forms
from .models import Asistencia_Empleado, Horario

class createAsistenciaForm(ModelForm):
    class Meta:
            model = Asistencia_Empleado
            fields = ['observacion']