from django.urls import path
from AppMedica import views,forms


urlpatterns = [
    
    path('inicio/', views.inicio, name='Inicio'),
    path('servicios/', views.servicios, name='Servicios'),
    path('pacientes/', views.pacientes, name='Pacientes'),
    path('medicos/', views.medicos, name='Medicos'),
    path('contacto/', views.contacto, name='Contacto'),
    path('medicoFormulario/',views.medicoFormulario,name="MedicoFormulario"),
    path('pacienteFormulario/',views.pacienteFormulario,name="PacienteFormulario"),
    path('contactoFormulario/',views.contactoFormulario,name='ContactoFormulario'),
    path ('busquedaMedico', views.busquedaMedico),
    path('buscarMedico/', views.buscarMedico),
    path ('busquedaPaciente', views.busquedaPaciente),
    path('buscarPaciente/', views.buscarPaciente),
    
    
    
    
    ]