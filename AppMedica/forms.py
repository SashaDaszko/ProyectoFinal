from django import forms
from django.db.models.fields import DateField
from django.forms.fields import EmailField, IntegerField,CharField
import datetime

class MedicoFormulario(forms.Form):
    #Especificar los campos
    
    apellido = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    matricula = IntegerField()
    email= EmailField()
    
class PacienteFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    fNac=forms.DateField(initial=datetime.date.today)
    telefono=forms.IntegerField()
    email=forms.EmailField()
    
class ContactoFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    tel=forms.IntegerField()
    mensaje=forms.CharField(max_length=250)