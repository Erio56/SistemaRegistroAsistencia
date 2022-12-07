from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError, OperationalError
from django.contrib.auth.decorators import login_required

from Assist.models import Asistencia_Empleado
from .forms import createAsistenciaForm
from .models import Horario, Asistencia_Empleado
from User.models import Empleado

import datetime
from django.utils import timezone

# Create your views here.
@login_required
def asistencia(request):
    return render(request, 'asistencia.html')

@login_required
def create_asistencia(request):
    epa = Empleado.objects.get(cuenta_usuario=request.user)
    if request.method == 'GET':
        now = timezone.now()
        now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        assists = Asistencia_Empleado.objects.filter(cedula=epa)
        assists.filter(fecha_hora_asitencia__gte=now)
        if assists.count() != 0:
            return render(request, 'createAsistencia.html',{
            'epa': epa,
            'flag_already_marked': True,
            'success': True,
            'home_flag': True 
            })
        else:            
            return render(request, 'createAsistencia.html', {
                'form': createAsistenciaForm,
                'epa':epa,
                'home_flag': True,
            })
    if request.method == 'POST':
        try:
            now = timezone.now()
            now = now.replace(hour=0, minute=0, second=0, microsecond=0)
            assists = Asistencia_Empleado.objects.filter(cedula=epa)
            assists.filter(fecha_hora_asitencia__gte=now)
            if assists.count() != 0:
                return render(request, 'createAsistencia.html',{
                'epa': epa,
                'flag_already_marked': True,
                'success': False,
                'home_flag': True,
                'error_message': 'La asistencia ya fue marcada'
            })
            form = createAsistenciaForm(request.POST)
            push = form.save(commit=False)
            push.cedula = Empleado.objects.get(cuenta_usuario=request.user)
            push.save()
            return render(request, 'createAsistencia.html',{
                'epa': epa,
                'success': True
            })
        except Exception as e:
            return render(request, 'createAsistencia.html',{
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
