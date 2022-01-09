from django.db import models
from django.db.models.fields import EmailField

class Medico(models.Model):

    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    matricula = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.especialidad}, {self.matricula},{self.email}"


class Paciente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fNac = models.DateField()
    telefono = models.IntegerField()
    email = models.EmailField(null=True)
    servicioSolicitado = models.CharField(max_length=40)
    
    
    def __str__(self):

        return f"{self.nombre}, {self.apellido}, {self.fNac}, {self.telefono}, {self.email}, {self.servicioSolicitado}"


class Servicio(models.Model):

    tipoServicio = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"{self.tipoServicio}, {self.especialidad}, {self.precio}"

class Contacto(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    tel=models.IntegerField()
    mensaje=models.CharField(max_length=250)
    
    def __str__(self):
        
        return f"{self.nombre},{self.apellido},{self.email},{self.tel},{self.mensaje}"