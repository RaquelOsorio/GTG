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
    fechaInicio = models.DateField(null=True)
    fechaFin= models.DateField(null=True)
    fechaMod= models.DateField(auto_now=True)
    nombre = models.CharField(max_length=32, unique=True)
    complejidad=models.IntegerField()
    #nrofase=models.IntegerField()
    estado = models.CharField(max_length=20,
                              choices=ESTADO_CHOICES,
                              default='PEN')
    lider= models.ForeignKey(User, related_name='lider')
    comite=models.ManyToManyField(User,blank=True, null=True)
    cantIntegrantes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.nombre

class Miembros(models.Model):
    integrante=models.ForeignKey(User)
    proyec=models.ForeignKey(Proyectos)
    cantidad=models.IntegerField()

class Fases1(models.Model):
    ESTADO_CHOICES=(
         ('INA','Inactiva'),
        ('PEN','Pendiente'),
        ('ACT','Activa'),
        ('FIN','Finalizada')
    )

    fechaInicio=models.DateField(null=True)
    fechaFin=models.DateField(auto_now=False)
    fechaMod= models.DateField(auto_now=True)
    nombre=models.CharField(max_length=32, unique=True)
    descripcion=models.TextField(max_length=100)
    estado = models.CharField(max_length=20,
                              choices=ESTADO_CHOICES,
                              default='INA')
    proyectos=models.ForeignKey(Proyectos, related_name='proyecto')

    def __unicode__(self):
        return self.nombre


class TipoAtributo(models.Model):
     nombre = models.CharField(max_length=32, unique=True)
     descripcion=models.TextField(max_length=100)
     def __unicode__(self):
         return self.nombre
     TIPO_CHOICES=(
        ('Entero', models.IntegerField),
        ('Cadena', models.CharField),
        ('Fecha',models.DateField),
        ('Mail', models.EmailField),
     )
     nombre = models.CharField(max_length=32, unique=True)
     descripcion=models.TextField(max_length=100)
     tipo= models.CharField(max_length=20,choices=TIPO_CHOICES,default='Entero')
     def __unicode__(self):
        return self.tipo

class TipoItem(models.Model):
    TATRIBUTO_CHOICES=(
         ('RF','Requerimientos Funcionales'),
        ('RNF','Requerimientos No Funcionales'),
    )
    nombre = models.CharField(max_length=32, unique=True)
    descripcion=models.TextField(max_length=100)
    tipoAtributo= models.ForeignKey(TipoAtributo)
    def __unicode__(self):
        return self.nombre


class RolUsuario(models.Model):
    rol= models.ForeignKey(Rol, unique=True)
    usuario=models.ForeignKey(User, unique=True)
    proyecto=models.ForeignKey(Proyectos)

    class Meta:
            unique_together = ('rol', 'usuario', 'proyecto')
        #    permissions=(("asociarRol","puede asociar roles a usuarios"),)




class Item(models.Model):
    E_REDACCION='REDAC'
    E_TERMINADO='TER'
    E_VALIDADO='VAL'
    E_DESACTIVADO='DESAC'
    E_REVISION='REV'
    ESTADO_CHOICES=(
        (E_REDACCION,'Redaccion'),
        (E_TERMINADO, 'Terminado'),
        (E_VALIDADO,'Validado'),
        (E_DESACTIVADO,'Desactivado'),
        (E_REVISION,'En_Revision'),
    )
        #Estado de una relacion
    E_ELIMINADO = 'DEL'
    E_ACTIVO = 'ACT'
    ESTADOS_RELACION = ((E_ELIMINADO, 'Eliminado'),(E_ACTIVO, 'Activo'))

    nombre=models.CharField(max_length=32, unique=False)
    version=models.IntegerField(max_length=32, default=1)
    prioridad=models.IntegerField(max_length=32)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=E_REDACCION, null=False,blank= False)
    descripcion=models.TextField(max_length=100)
    fechaModi=models.DateField(auto_now=True)
    tipoItem=models.ForeignKey(TipoItem)
    fase=models.ForeignKey(Fases1, related_name='fase')

    antecesorHorizontal= models.ForeignKey('self',related_name='RantecesorHorizontal',null=True, blank= True)
    sucesorHorizontal= models.ForeignKey('self',related_name='RsucesorHorizontal',null=True, blank= True)
    sucesorVertical= models.ForeignKey('self',related_name='RsucesorVertical',null=True, blank= True)
    antecesorVertical=models.ForeignKey('self',related_name='RantecesorVertical',null=True, blank=True)
    relacion= models.CharField(max_length=20, choices= ESTADOS_RELACION, null=True, blank=True)

    def __unicode__(self):
         return self.nombre

        #class Meta:
        #    permissions=(("asociarRol","puede asociar roles a usuarios"),)



class lineaBase(models.Model):

    E_ABIERTA='ABIERTA'
    E_CERRADA='CERRADA'
    E_ROTA='ROTA'
    E_REVISION='REVISION'
    ESTADO_CHOICES=(
        (E_ABIERTA,'Abierta'),
        (E_CERRADA, 'Cerrada'),
        (E_ROTA,'Rota'),
        (E_REVISION,'En_Revision'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=E_ABIERTA, null=False,blank= False)
    fase= models.ForeignKey(Fases1,null=True, blank= True)
    itemsAsociados= models.ForeignKey(Item,null=True, blank= True)

    def __unicode__(self):
         return self.estado


class ItemRelacion(models.Model):
    """

    :Model: ItemRelacion
    Modelo que permite almacenar las relaciones entre items.
    Items de una misma fase.
    Items de fases antecesoras.

    """
    #Estado de una relacion
    ESTADO_CHOICES=(
        ('DEL','Eliminado'),
        ('ACT', 'Activo'),
    )
    estado = models.CharField(max_length=20,
                              choices=ESTADO_CHOICES,
                              default='ACT')

    #Tipo de relacion : interno (Intrafase) o externa(InterFase)
    E_INT = 'I'
    E_EXT = 'E'
    TIPO_CHOICES=(
        (E_INT,'Padre -> Hijo'),
        (E_EXT, 'Antecesor -->> Sucesor'),
    )
    tipo = models.CharField(max_length=20,
                              choices=TIPO_CHOICES)
    origen = models.ForeignKey(Item, related_name="origen")
    destino = models.ForeignKey(Item,related_name="destino")
    def set_tipo(self):
        if self.origen.fase == self.destino.fase:
            self.tipo = self.E_INT
        else:
            self.tipo = self.E_EXT

class Comite(models.Model):
    #proyecto= models.ForeignKey(Proyectos, unique=False,null=True, blank= True)
    usuario=models.ForeignKey(User,null=True, blank= True)
    cantidad_integrantes=models.IntegerField(default=0)

