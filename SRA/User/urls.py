from django.urls import include, path

from rest_framework import routers, viewsets

from . import views
from .api import EmpleadoViewSet, CargoViewSet, DependenciaViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'api/empleado', EmpleadoViewSet, 'empleado')
router.register(r'api/cargo', CargoViewSet, 'cargo')
router.register(r'api/dependencia', DependenciaViewSet, 'dependencia')
router.register(r'users', UserViewSet)


# urlpatterns = router.urls

#OLD
urlpatterns = [
    path('logout/', views.signOut, name='logout'),
    path('signin/', views.signIn, name='signin'),
    path('signup/', views.signUp, name='signup'),
    path('admin/createDependencia', views.createDependencia, name='createDependencia'),
    path('admin/createCargo/', views.createCargo, name='createCargo'),
    path('', views.home, name='home'),
]