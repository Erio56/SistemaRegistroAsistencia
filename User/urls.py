from django.urls import path

from . import views


urlpatterns = [
    path('logout/', views.signOut, name='logout'),
    path('signin/', views.signIn, name='signin'),
    path('signup/', views.signUp, name='signup'),
    path('', views.home, name='home'),
]