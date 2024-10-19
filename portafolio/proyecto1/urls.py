from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home2),
    path('registrarTarea/', views.registarTarea),
    path('eliminarTarea/<Title>', views.eliminarTarea),
    path('ActualizarTarea/', views.ActualizarTarea),
    path('leerTarea/<Title>', views.leerTarea),
    path('LeerTarea/', views.LeerTarea),
    path('actualizarTarea/<Title>', views.actualizarTarea),
]