from django.urls import path

from . import views


urlpatterns = [
    path('asistencia/marcar', views.create_asistencia, name='createAsistencia'),
    path('asistencia/listar', views.listAsistencias, name="listAsists"),
    path('horario/crear', views.create_horario, name="createHorario"),
]