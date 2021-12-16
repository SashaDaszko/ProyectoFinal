from django import forms
from django.db.models.fields import DateField
from django.forms.fields import EmailField, IntegerField

class MedicoFormulario(forms.Form):
    #Especificar los campos
    
    apellido = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    matricula = IntegerField()
    email= EmailField()
    
class PacienteFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)    
    telefono=forms.IntegerField()
    fNac=forms.IntegerField()
    
class ContactoFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    tel=forms.IntegerField()
    mensaje=forms.CharField(max_length=250)