from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def vacation_registier(request):
   # TODO
   pass

def permition_register(request):
   # TODO
   pass

def list_vacation(request):
   # TODO
   pass


@login_required
def list_permits(request):
   return render(request, 'listPermits.html')