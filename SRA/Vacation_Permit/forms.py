from django import forms
from Vacation_Permit.models import PermisoEmpleado

class CreatePermisoForm(forms.ModelForm):
    class Meta:
        model = PermisoEmpleado
        fields = ['fecha_final', 'fecha_inicio', 'descripcion']
        widgets = {
           'fecha_inicio': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'class': 'input',
                    'min':'1900-01-01', 
                    'max':'2100-01-01',
                    'onfocus':'this.min=new Date().toISOString().split('"'T'"')[0]'
                    }),
           'fecha_final': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'class': 'input',
                    'min':'1900-01-01', 
                    'max':'2100-01-01',
                    'onfocus':'this.min=new Date().toISOString().split('"'T'"')[0]'
                    }),
           'descripcion': forms.TextInput(attrs={
                 'class': 'input'
              })
            }