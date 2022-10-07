from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError, OperationalError
from django.contrib.auth.decorators import login_required

from Assist.models import Asistencia_Empleado
from .forms import createAsistenciaForm

from User.models import Empleado


# Create your views here.
@login_required
def asistencia(request):
    return render(request, 'asistencia.html')

@login_required
def create_asistencia(request):
    epa = Empleado.objects.get(cuenta_usuario=request.user)
    if request.method == 'GET':
        return render(request, 'createasistencia.html', {
            'form': createAsistenciaForm,
            'epa':epa,
            'home_flag': True,
        })
    else:
        try:
            form = createAsistenciaForm(request.POST)
            push = form.save(commit=False)
            print(push)
            push.cedula = Empleado.objects.get(cuenta_usuario=request.user)
            push.save()
            return render(request, 'createasistencia.html',{
                'epa': epa,
                'form': createAsistenciaForm,
                'success': True
            })
        except Exception as e:
            return render(request, 'createasistencia.html',{
                'epa': epa,
                'form': createAsistenciaForm,
                'success': False
            })


@login_required
def listAsistencias(request):
    assists = Asistencia_Empleado.objects.filter( cedula = Empleado.objects.get(cuenta_usuario=request.user)).order_by('-fecha_hora_asitencia')
    epa = Empleado.objects.get(cuenta_usuario=request.user)
    return render(request, 'listAsistencia.html', {'Asistencias': assists,
                                                   'epa': epa })
