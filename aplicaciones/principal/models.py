from django.db import models
from django.utils import timezone
class Persona(models.Model):
    tiempo=timezone.now()
    id= models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)    
    correo = models.EmailField(max_length=200)
    dni = models.IntegerField(default=None)
    domicilio  = models.CharField(max_length=100, default='Calle Falsa 123')
    nac = models.DateField(default=None)
    alta_sistema = tiempo

    def __str__(self):
        return self.nombre+" "+self.apellido