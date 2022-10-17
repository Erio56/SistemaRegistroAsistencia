from tkinter import Widget
from turtle import textinput
from django.forms import ModelForm, fields
from django import forms
from .models import Cargo, Dependencia, Empleado


from django.forms import ModelChoiceField




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
        fields = ['nombres', 'apellidos', 'direccion', 'telefono', 'fecha_nacimiento','cedula', 'cargo', 'email']
        widgets = {
            'cedula': forms.NumberInput(attrs={
                'class':'input'}) ,
            'nombres': forms.TextInput(attrs={
                'class':'input'
                }) , 
            'apellidos': forms.TextInput(attrs={
                'class':'input'
                }),
            'email': forms.EmailInput(attrs={
                'class':'input'}),  
            'direccion': forms.TextInput(attrs={
                'class':'input'
                }), 
            'telefono': forms.NumberInput(attrs={
                'class':'input'}),
            
            'cargo': forms.Select(),
            'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'class': 'input',
                    'min':'1900-01-01', 
                    'max':'2100-01-01',
                    
                    'onfocus':'this.max=new Date().toISOString().split('"'T'"')[0]'
                    
                    }
                )
            }
