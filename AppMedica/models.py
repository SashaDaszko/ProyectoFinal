from django.db import models

class Medico(models.Model):

    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    matricula = models.IntegerField()
<<<<<<< HEAD
    email = models.EmailField()

=======
    email=models.EmailField()
    
>>>>>>> c6470f2b09bf1f266569cc86fc47ffd7c76d8653
    def __str__(self):
        return f"{self.apellido}, {self.especialidad}, {self.matricula},{self.email}"


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

