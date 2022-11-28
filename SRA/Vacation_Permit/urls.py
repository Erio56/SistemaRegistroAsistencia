from django.urls import path

from . import views

urlpatterns = [
    path('permiso/crear', views.permition_register, name='register_permit'),
    path('permiso/listado', views.list_permits, name='list_permit'),
    #path('vaciones/editar', views.index, name='index'),
]