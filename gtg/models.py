#encoding:utf-8
from django.db import models

# Create your models here.

class inicio_sesion(models.Model):
        nombre = models.CharField(max_length=50)
        contrasena = models.TextField(help_text='8 caracteres como minimo')
        confirmar = models.TextField()

        def __unicode__(self):
            return self.nombre


