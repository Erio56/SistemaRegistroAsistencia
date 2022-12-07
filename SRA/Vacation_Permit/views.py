from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

import datetime

from User.models import Empleado
from Vacation_Permit.models import PermisoEmpleado, VacacionesEmpleado
from Vacation_Permit.forms import CreatePermisoForm, CreateVacationForm

# Create your views here.

@login_required
def vacation_registier(request):
   user = Empleado.objects.get(cuenta_usuario=request.user)
   if request.method == 'GET':
      return render(request, 'createVacation.html',{
         'form': CreateVacationForm
      })
   if request.method == 'POST':
      form_recived = CreateVacationForm(request.POST)
      push = form_recived.save(commit=False)
      push.cedula = user
      push.fecha_solicitud = timezone.now()
      if push.fecha_inicio < push.fecha_final:
         push.save()
         success = True
         return render(request, 'createVacation.html',{
            'form': CreatePermisoForm,
            'success': success,
            'epa': user
         })
      else:
         return render(request, 'createVacation.html',{
            'form': form_recived,
            'success': False,
            'error_msg': 'La fecha final no puede ser mayor a la fecha inicial',
            'epa': user
         })


@login_required
def permition_register(request):
   user = Empleado.objects.get(cuenta_usuario=request.user)
   if request.method == 'GET':
      return render(request, 'createPermiso.html',{
         'form': CreatePermisoForm
      })
   if request.method == 'POST':
      form_recived = CreatePermisoForm(request.POST)
      push = form_recived.save(commit=False)
      push.cedula = user
      push.fecha_solicitud = timezone.now()
      if push.fecha_inicio < push.fecha_final:
         push.save()
         success = True
         return render(request, 'createPermiso.html',{
            'form': CreatePermisoForm,
            'success': True,
            'epa': user
         })
      else:
         return render(request, 'createPermiso.html',{
            'form': form_recived,
            'success': False,
            'error_msg': 'La fecha final no puede ser mayor a la fecha inicial',
            'epa': user
         })


@login_required
def list_vacation(request):
   empleado = Empleado.objects.get(cuenta_usuario=request.user)
   vacations = VacacionesEmpleado.objects.filter(cedula=empleado).order_by('-fecha_solicitud')
   return render(request, 'listVacations.html', {
      'vacations': vacations,
      'epa': empleado
   })

@login_required
def list_permits(request):
   empleado = Empleado.objects.get(cuenta_usuario=request.user)
   permits = PermisoEmpleado.objects.filter(cedula=empleado).order_by('-fecha_solicitud')
   return render(request, 'listPermits.html', {
      'permits': permits,
      'epa': empleado
   })