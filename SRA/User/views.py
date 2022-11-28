from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError, OperationalError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


from User.forms import CustomUserCreationForm, createDependenciaForm, CreateEmpleadoForm, createCargoForm, UpdateEmpleadoForm, CustomLoginForm
from User.models import Cargo, Empleado, Dependencia

# Create your views here.


def home(request):
    if request.user.id != None:
        epa = Empleado.objects.get(cuenta_usuario=request.user)
    else:
        epa = "Visitante"
    return render(request, 'home.html', {
        'epa': epa
    })

def signUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm,
            'form2': CreateEmpleadoForm,
        })
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                formu = CreateEmpleadoForm(request.POST)
                formu.is_valid()
                form = formu.cleaned_data
                empleado_temp = Empleado(cedula=form['cedula'], cuenta_usuario=user, nombres=form['nombres'], apellidos=form['apellidos'],
                                             direccion=form['direccion'], telefono=form['telefono'], fecha_nacimiento=form['fecha_nacimiento'])
                empleado_temp.save()
                login(request, user)
                return redirect('home')

    user.delete()
    return render(request, 'signup.html', {
                        'form': CustomUserCreationForm,
                        'form2': CreateEmpleadoForm,
                        'error': formu.errors
                    })

def signOut(request):
    logout(request)
    return redirect(home)


def signIn(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': CustomLoginForm,
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': CustomLoginForm,
                'error': 'Password or user invalid',
            })
        else:
            login(request, user)
            return redirect(home)

@login_required
def createCargo(request):
    if request.method == 'GET':
        return render(request, 'createCargo.html', {
            'form': createCargoForm,
        })
    elif request.method == 'POST':
        try:
            cargo_temp = Cargo(nombre_cargo=request.POST['nombre_cargo'], dependencia=Dependencia.objects.get(id=request.POST['dependencia']))
            cargo_temp.save()
            return render(request, 'createCargo.html', {
                'form': createCargoForm,
                'status': 'Registrado correctamente',
                'epa': Empleado.objects.get(cuenta_usuario=request.user)
            })
        except IntegrityError:
            return render(request, 'createCargo.html', {
                'form': createCargoForm,
                'status': 'Error: el cargo ya existe',
                'epa': Empleado.objects.get(cuenta_usuario=request.user)
            })
    else:
        return render(request, 'createCargo.html', {
            'form': createCargoForm,
            'status': 'Hubo un error en el sistema.',
            'epa': Empleado.objects.get(cuenta_usuario=request.user)
        })
        
        
@login_required
def createDependencia(request):
    if request.method == 'GET':
        return render(request, 'createDependencia.html', {
            'form': createDependenciaForm,
            'epa': Empleado.objects.get(cuenta_usuario=request.user)
        })
    elif request.method == 'POST':
        try:
            dependencia_temp = Dependencia(nombre_dependencia=request.POST['nombre_dependencia'])
            dependencia_temp.save()
            return render(request, 'createDependencia.html', {
                'form': createDependenciaForm,
                'status': 'Registrado correctamente',
                'epa': Empleado.objects.get(cuenta_usuario=request.user)
            })
        except IntegrityError:
            return render(request, 'createDependencia.html', {
                'form': createDependenciaForm,
                'status': 'Error: el cargo ya existe',
                'epa': Empleado.objects.get(cuenta_usuario=request.user)
            })
    else:
        return render(request, 'createDependencia.html', {
            'form': createDependenciaForm,
            'status': 'Hubo un error en el sistema.',
            'epa': Empleado.objects.get(cuenta_usuario=request.user)
        })
        
        
@login_required
def updateUser(request):
        if request.method == 'GET':
            empleado = Empleado.objects.get(cuenta_usuario=request.user)
            form = UpdateEmpleadoForm(instance=empleado)
            return render(request, 'userUpdate.html', {
                'form': form,
                'epa': empleado,
        })
        elif request.method == 'POST':
            try:
                empleado = Empleado.objects.get(cuenta_usuario=request.user)
                form2 = UpdateEmpleadoForm(request.POST, instance=empleado)
                if form2.is_valid():
                    form2.save()
                    return render(request, 'userUpdate.html', {
                    'form': form2,
                    'status': True,
                    'epa': empleado
                    })
                else:
                    print(form2.cleaned_data)
                    error = form2.errors
                    return render(request, 'userUpdate.html', {
                        'error': error,
                        'form': form2,
                        'epa': Empleado.objects.get(cuenta_usuario=request.user)
                })
            except IntegrityError:
                return render(request, 'userUpdate.html', {

                    'epa': Empleado.objects.get(cuenta_usuario=request.user)
                })
        else:
            return render(request, 'errorpage.html', {
                    'status': 'Error: contacte al administrador',
                    'epa': Empleado.objects.get(cuenta_usuario=request.user)
                })