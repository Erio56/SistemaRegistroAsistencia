from django.urls import path

from . import views

urlpatterns = [
    path('permiso/crear', views.permition_register, name='register_permit'),
    path('permiso/listado', views.list_permits, name='list_permit'),
    path('vacacion/crear', views.vacation_registier, name='vacation_register'),
    path('vacacion/listado', views.list_vacation, name='vacation_list'),
]