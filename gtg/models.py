#encoding:utf-8
from django.db import models

# Create your models here.


class Rol(models.Model):
    codigo = models.CharField(max_length=32, primary_key= True, unique=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __unicode__(self):
        return self.nombre



class Proyecto(models.Model):
    fechaInicio = models.DateField(max_length=30)
    nombre = models.CharField(max_length=32, unique=True)
    complejidad=models.IntegerField()
    estado = "PEN"
    def __unicode__(self):
        return self.codigo