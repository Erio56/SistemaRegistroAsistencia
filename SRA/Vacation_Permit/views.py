from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from User.models import Empleado
from Vacation_Permit.forms import CreatePermisoForm
# Create your views here.

@login_required
def vacation_registier(request):
   # TODO
   pass

@login_required
def permition_register(request):
   if request.method == 'GET':
      return render(request, 'createPermiso.html',{
         'form': CreatePermisoForm
      })
   if request.method == 'POST':
      form_recived = CreatePermisoForm(request.POST)
      push = form_recived.save(commit=False)
      user = Empleado.objects.get(cuenta_usuario=request.user)
      print(user)
      push.cedula = user
      push.save()
      success = True
      return render(request, 'createPermiso.html',{
         'form': CreatePermisoForm,
         'success': success,
         'epa': user
      })


@login_required
def list_vacation(request):
   # TODO
   pass


@login_required
def list_permits(request):
   
   return render(request, 'listPermits.html')