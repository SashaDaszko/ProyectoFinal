from django.urls import path
from AppMedica import views,forms

#PARA EL LOGOUT
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('inicio/', views.inicio, name='Inicio'),
    path('servicios/', views.servicios, name='Servicios'),
    path('pacientes/', views.pacientes, name='Pacientes'),
    path('medicos/', views.medicos, name='Medicos'),
    path('contacto/', views.contacto, name='Contacto'),
    path('medicoFormulario/',views.medicoFormulario,name="MedicoFormulario"),
    path('pacienteFormulario/',views.pacienteFormulario,name="PacienteFormulario"),
    path('contactoFormulario/',views.contactoFormulario,name='ContactoFormulario'),
    path('busquedaMedico', views.busquedaMedico),
    path('buscarMedico/', views.buscarMedico),
    path('busquedaPaciente', views.busquedaPaciente, name="BusquedaPaciente"),
    path('buscarPaciente/', views.buscarPaciente),
    path('about',views.about,name="About"),
    
    #CRUD
    path('leerMedicos', views.leerMedicos, name='LeerMedicos'),
    path('eliminarMedicos/<matricula_para_borrar>/', views.eliminarMedicos, name="EliminarMedicos"),
    path('editarMedicos/<matricula_para_editar>/', views.editarMedicos, name="EditarMedicos"),
    
    
    
    
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    
    path('logout', LogoutView.as_view(template_name='AppMedica/logout.html'), name="Logout"),
    
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar")
    
    
    
    
    
]
