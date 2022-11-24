from django.urls import path

from . import views

urlpatterns = [
    path('permiso/crear', views.list_permits, name='list_permits'),
    #path('vaciones/ver', views.index, name='index'),
    #path('vaciones/editar', views.index, name='index'),
]