from django.shortcuts import render
from django.http import HttpResponse

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