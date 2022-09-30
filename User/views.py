from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError, OperationalError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser



from User.forms import linkEmpleadoForm
from User.models import Empleado


# Create your views here.

def home(request):
    if request.user.id != None:
        epa = Empleado.objects.get(cuenta_usuario=request.user)
    else:
        epa = "Visitante"
    return render(request, 'home.html',{
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
                print(formu.is_valid())
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
        
