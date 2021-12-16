from django.shortcuts import render
from django.http import HttpResponse
from AppMedica.models import Medico,Paciente,Servicio,Contacto
from AppMedica.forms import MedicoFormulario,ContactoFormulario,PacienteFormulario

def contactoFormulario (request):
    
    #Obtiene la direccion el anioFund
    if request.method == "POST":
        
        miFormulario = ContactoFormulario(request.POST)
        
        if miFormulario.is_valid():  # va con ()
            
            informacion = miFormulario.cleaned_data
        
            contactoInsta = Contacto(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],tel=informacion["tel"],mensaje=informacion["mensaje"])
            
            contactoInsta.save()  #Este save guarda en la base de datos
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = ContactoFormulario()
    
    #return HttpResponse ("Esto es una prueba de inicio")
    return render(request,'AppMedica/contactoFormulario.html',{"miFormulario":miFormulario})

def pacienteFormulario (request):
    
    #Obtiene la direccion el anioFund
    if request.method == "POST":
        
        miFormulario = PacienteFormulario(request.POST)
        
        if miFormulario.is_valid():  # va con ()
            
            informacion = miFormulario.cleaned_data
        
            pacienteInsta = Paciente(nombre=informacion["nombre"], apellido=informacion["apellido"],telefono=informacion["telefono"],fNac=informacion["FNac"])
            
            pacienteInsta.save()  #Este save guarda en la base de datos
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = PacienteFormulario()
    
    #return HttpResponse ("Esto es una prueba de inicio")
    return render(request,'AppMedica/pacienteFormulario.html',{"miFormulario":miFormulario})


def medicoFormulario (request):
   
    #Obtiene la direccion el anioFund
    if request.method == "POST":
        
        miFormulario = MedicoFormulario(request.POST)
        
        if miFormulario.is_valid():  # va con ()
            
            informacion = miFormulario.cleaned_data
        
            medicoInsta = Medico(apellido=informacion["apellido"], especialidad=informacion["especialidad"],matricula=informacion["matricula"],email=informacion["email"])
            
            medicoInsta.save()  #Este save guarda en la base de datos
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = MedicoFormulario()
    
    #return HttpResponse ("Esto es una prueba de inicio")
    return render(request,'AppMedica/medicoFormulario.html',{"miFormulario":miFormulario})



def inicio(request):

    return render(request,'AppMedica/inicio.html')


def servicios(request):

    return render(request,'AppMedica/servicios.html')


def pacientes(request):

    return render(request,'AppMedica/pacientes.html')


def medicos(request):

    return render(request,'AppMedica/medicos.html')



def contacto(request):

    return render(request,'AppMedica/contacto.html')

