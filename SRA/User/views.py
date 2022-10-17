from operator import ge
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError, OperationalError
from django.contrib.auth.decorators import login_required



from User.forms import createDependenciaForm, linkEmpleadoForm, createCargoForm
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
            'form': UserCreationForm,
            'form2': linkEmpleadoForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                formu = linkEmpleadoForm(request.POST)
                form = formu.cleaned_data
                try:
                    empleado_temp = Empleado(cedula=form['cedula'], cuenta_usuario=user, nombres=form['nombres'], apellidos=form['apellidos'],
                                             direccion=form['direccion'], telefono=form['telefono'], fecha_nacimiento=form['fecha_nacimiento'])
                    empleado_temp.save()
                except Exception as e:
                    user.delete()
                    return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'form2': linkEmpleadoForm,
                        'error': e
                    })
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'form2': linkEmpleadoForm,
                    'error': 'Username already exists'
                })
            except OperationalError:
                return render(request, 'linkEmpleadoAccount.html', {
                    'form': linkEmpleadoForm,
                    'error': 'Empleado con cedula {cedula}'.format(cedula=empleado_temp.cedula)
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'form2': linkEmpleadoForm,
            'error': 'Password do not match'
        })


def signOut(request):
    logout(request)
    return redirect(home)


def signIn(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
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
            form = linkEmpleadoForm(instance=empleado)
            return render(request, 'userUpdate.html', {
                'form': form,
                'epa': empleado
        })
        elif request.method == 'POST':
            try:
                empleado = get_object_or_404(Empleado, cuenta_usuario=request.user)
                form2 = linkEmpleadoForm(request.POST, instance=empleado)
                success = False
                if form2.is_valid():
                    form2.save()
                    success = True
                return render(request, 'userUpdate.html', {
                    'form': form2,
                    'success': success,
                    'status': 'Actualizado correctamente',
                    'epa': empleado
                })
            except IntegrityError:
                return render(request, 'errorpage.html', {
                    'status': 'Error: contacte al administrador',
                    'epa': Empleado.objects.get(cuenta_usuario=request.user)
                })
        else:
            return render(request, 'errorpage.html', {
                    'status': 'Error: contacte al administrador',
                    'epa': Empleado.objects.get(cuenta_usuario=request.user)
                })