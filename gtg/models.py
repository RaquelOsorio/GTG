#encoding:utf-8
from django.db import models

# Create your models here.

class inicio_sesion(models.Model):
    nombre = models.CharField(max_length=50)
    contrasena = models.TextField(help_text='8 caracteres como minimo')

    def __unicode__(self):
        """Esta es la clase del login
        @param nombre: nombre del usuario
        @param contrasena: contrasena del usuario
        @reuturn: retorna el nombre
        import: importa los modelos de django"""
        return self.nombre


