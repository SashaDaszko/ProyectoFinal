from django import forms
from django.forms.fields import EmailField, IntegerField

class MedicoFormulario(forms.Form):
    #Especificar los campos
    
    apellido = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    matricula = IntegerField()
    email= EmailField()
    
    
