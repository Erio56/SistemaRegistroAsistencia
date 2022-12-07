from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError, OperationalError
from django.contrib.auth.decorators import login_required

from Assist.models import Asistencia_Empleado
from .forms import createAsistenciaForm, createHoraForm
from .models import Horario, Asistencia_Empleado, Horario
from User.models import Empleado
from Assist.models import Hora, Horario
from .utils import str_to_time

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
                                                   'epa': epa})

def create_horario(request):
    epa = Empleado.objects.get(cuenta_usuario=request.user)
    if request.method == 'GET':
        return render(request, 'createHorario.html',{
            'formLunes': createHoraForm,
            'formMartes': createHoraForm,
            'formMiercoles': createHoraForm,
            'formJueves': createHoraForm,
            'formViernes': createHoraForm,
            'formSabado': createHoraForm,
            'formDomingo': createHoraForm,
            'epa': epa
        })
    if request.method == 'POST':
        hora_entradas = request.POST.getlist('hora_entrada')
        hora_salidas = request.POST.getlist('hora_salida')
        horario = Horario()
        for i in range(0,7):
            hora_entrada = str_to_time(hora_entradas[i])
            hora_salida = str_to_time(hora_salidas[i])
            print(hora_entrada)
            print(hora_salida)
            if hora_entrada != None and hora_salida != None:
                if hora_salida <= hora_salida:
                    if i == 0:
                        h = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h.save()
                        horario.lunes = h
                    elif i == 1:
                        h1 = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h1.save()
                        horario.martes = h1
                    elif i == 2:
                        h2 = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h2.save()
                        horario.miercoles = h2
                    elif i == 3:
                        h3 = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h3.save()
                        horario.jueves = h3
                    elif i == 4:
                        h4 = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h4.save()
                        horario.viernes = h4
                    elif i == 5:
                        h5 = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h5.save()
                        horario.sabado = h5
                    elif i == 6:
                        h6 = Hora(hora_entrada=hora_entrada,hora_salida=hora_salida)
                        h6.save()
                        horario.domingo = h6
        horario.empleado = epa
        horario.save()
        
        return render(request, 'createHorario.html', {
            'formLunes': createHoraForm,
            'formMartes': createHoraForm,
            'formMiercoles': createHoraForm,
            'formJueves': createHoraForm,
            'formViernes': createHoraForm,
            'formSabado': createHoraForm,
            'formDomingo': createHoraForm,
            'epa': epa
        })