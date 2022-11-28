from django import forms
from .models import Cargo, Dependencia, Empleado


from django.forms import ModelChoiceField

class createCargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre_cargo', 'dependencia']
        widgets = {
            'nombre_cargo': forms.TextInput(attrs={
                'class': 'input'
            }),
            'dependencia': forms.Select(attrs={
                'class': 'input',
                'placeholder': 'Seleciona una dependencia'
            })
        }
        
        
class createDependenciaForm(forms.ModelForm):
    class Meta:
        model = Dependencia
        fields = ['nombre_dependencia']
        widgets = {
            'nombre_dependencia': forms.TextInput(attrs={
                'class': 'input'
            }),
        }


class CreateEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado    
        fields = ['nombres', 'apellidos', 'direccion', 'telefono', 'fecha_nacimiento','cedula', 'cargo', 'email']
        widgets = {
            'cuenta_usuario': forms.Select(attrs={
                'class':'input',
                # 'disabled': True
                }),
            'cedula': forms.TextInput(attrs={
                'class':'input',
                # 'disabled': True
                }),
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
            'email': forms.EmailInput(attrs={
                'class':'input',
                }),
            'telefono': forms.NumberInput(attrs={
                'class':'input'}),
            'cargo': forms.Select(attrs={
                'required': False,
                'class':'input'}),
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

class UpdateEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'cuenta_usuario': forms.HiddenInput(attrs={
                'readonly':'readonly',
                'class':'input',
                # 'disabled': True
                }),
            'cedula': forms.HiddenInput(attrs={
                'readonly':'readonly',
                'class':'input',
                # 'disabled': True
                }),
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
            'email': forms.EmailInput(attrs={
                'class':'input',
                }),
            'telefono': forms.NumberInput(attrs={
                'class':'input'}),
            'cargo': forms.Select(attrs={
                'class':'input'}),
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
        
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'input'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'input'}
    )
    
class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'input'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'input'}
        )