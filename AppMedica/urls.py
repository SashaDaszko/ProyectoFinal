from django.urls import path
from AppMedica import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('servicios', views.servicios, name='Servicios'),
    path('pacientes', views.pacientes, name='Pacientes'),
    path('medicos', views.medicos, name='Medicos'),
    path('contacto', views.contacto, name='Contacto'),

    ]