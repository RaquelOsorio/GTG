#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
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
<<<<<<< HEAD
        return self.codigo
=======
        return self.dni
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
