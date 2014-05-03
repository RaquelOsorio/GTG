#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
# Create your models here.

class Usuario(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    mail = models.EmailField()


class Usuario_rol(models.Model):
    usuario = models.ForeignKey(User)
    des= models.TextField()
        #rol = models.ForeignKey()

class Rol(models.Model):
    codigo = models.CharField(max_length=32, primary_key= True, unique=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    controlTotal=models.BooleanField()
    creacionLB=models.BooleanField()
    rupturaLB=models.BooleanField()
    consultaLB=models.BooleanField()
    crearItem=models.BooleanField()
    modificarItem=models.BooleanField()
    eliminarItem=models.BooleanField()
    reversionarItem=models.BooleanField()
    aprobarItem=models.BooleanField()
    desaprobarItem=models.BooleanField()
    consultaItem=models.BooleanField()
    impactoItem=models.BooleanField()
    class Meta:
        permissions=(("asociar","puede asociar permisos"),)

    def __unicode__(self):
        return self.nombre

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Proyectos(models.Model):
    ESTADO_CHOICES=(
        ('PEN','Pendiente'),
        ('ANU','Anulado'),
        ('ACT','Activo'),
        ('FIN','Finalizado')
    )
    fechaInicio = models.DateField()
    nombre = models.CharField(max_length=32, unique=True)
    complejidad=models.IntegerField()
    #nrofase=models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    lider= models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre

class Fases1(models.Model):
    ESTADO_CHOICES=(
         ('INA','Inactiva'),
        ('PEN','Pendiente'),
        ('ACT','Activa'),
        ('FIN','Finalizada')
    )

    fechaInicio=models.DateField(auto_now=True)
    fechaFin=models.DateField(auto_now=False)
    nombre=models.CharField(max_length=32, unique=True)
    descripcion=models.TextField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    proyectos=models.ForeignKey(Proyectos)
    def __unicode__(self):
        return self.nombre


class ModificarRol(models.Model):
    rol= models.ForeignKey(Rol)
    fecha= models.DateField(auto_now=True)

class TipoAtributo(models.Model):
     codigo = models.CharField(max_length=32, primary_key= True, unique=True)
     nombre = models.CharField(max_length=32, unique=True)
     descripcion=models.TextField(max_length=100)
     def __unicode__(self):
         return self.nombre

class TipoItem(models.Model):
    TATRIBUTO_CHOICES=(
         ('RF','Requerimientos Funcionales'),
        ('RNF','Requerimientos No Funcionales'),
    )
    codigo = models.CharField(max_length=32, primary_key= True, unique=True)
    nombre = models.CharField(max_length=32, unique=True)
    descripcion=models.TextField(max_length=100)
    tipoAtributo= models.ForeignKey(TipoAtributo)
    def __unicode__(self):
        return self.nombre


class RolUsuario(models.Model):
    rol= models.ForeignKey(Rol)
    usuario=models.ForeignKey(User)
    proyecto=models.ForeignKey(Proyectos)

        #class Meta:
        #    permissions=(("asociarRol","puede asociar roles a usuarios"),)



class TipoAtributo(models.Model):
     codigo = models.CharField(max_length=32, primary_key= True, unique=True)
     nombre = models.CharField(max_length=32, unique=True)
     descripcion=models.TextField(max_length=100)
     def __unicode__(self):
         return self.nombre


class Item(models.Model):
    ESTADO_CHOICES=(
        ('REDAC','Redaccion'),
        ('TER', 'Terminado'),
        ('VAL','Validado'),
        ('DESAC','Desactivado'),
        ('REV','En_Revision'),
    )
    nroItem=models.IntegerField(max_length=32, primary_key= True, unique=True)
    nombre=models.CharField(max_length=32, unique=True)
    version=models.IntegerField(max_length=32)
    prioridad=models.IntegerField(max_length=32)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    descripcion=models.TextField(max_length=100)
    fechaModi=models.DateField(auto_now=True)
    tipoItem=models.ForeignKey(TipoItem)
    fase=models.ForeignKey(Fases1)
    antecesorHorizontal= models.OneToOneField('self',related_name='RantecesorHorizontal',null=True, blank= True)
    antecesorVertical=models.OneToOneField('self',related_name='RantecesorVertical',null=True, blank=True)
    def __unicode__(self):
         return self.nombre

        #class Meta:
        #    permissions=(("asociarRol","puede asociar roles a usuarios"),)


