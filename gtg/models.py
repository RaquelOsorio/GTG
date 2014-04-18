#encoding:utf-8
from django.db import models

# Create your models here.





class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.dni