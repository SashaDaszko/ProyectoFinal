from django.db import models

class Medico(models.Model):

    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    matricula = models.IntegerField()

    def __str__(self):
        return f"{self.apellido}, {self.especialidad}, {self.matricula}"


class Paciente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fNac = models.DateField()

    def __str__(self):

        return f"{self.nombre}, {self.apellido}, {self.telefono}, {self.fNac}"


class Servicio(models.Model):

    tipoServicio = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"{self.tipoServicio}, {self.especialidad}, {self.telefono}, {self.precio}"

