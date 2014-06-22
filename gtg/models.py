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

    creacionLB=models.BooleanField()
    crearTipoItem=models.BooleanField()
    crearItem=models.BooleanField()
    modificarItem=models.BooleanField()
    eliminarItem=models.BooleanField()
    reversionarItem=models.BooleanField()
    relacionarItem=models.BooleanField()
    revivirItem=models.BooleanField()
    aprobarItem=models.BooleanField()
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
    estado = models.CharField(max_length=20,
                              choices=ESTADO_CHOICES,
                              default='PEN')
    lider= models.ForeignKey(User, related_name='lider')
    comite=models.ManyToManyField(User,blank=True, null=True)
    def __unicode__(self):
        return self.nombre

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
    nombre=models.CharField(max_length=32, unique=False)
    cantidadItem=models.IntegerField(max_length=32)
    descripcion=models.TextField(max_length=100)
    orden = models.SmallIntegerField(verbose_name='Orden')
    estado = models.CharField(max_length=20,
                              choices=ESTADO_CHOICES,
                              default='INA')
    proyectos=models.ForeignKey(Proyectos, related_name='proyecto')

    def __unicode__(self):
        return self.nombre


class TipoAtributo(models.Model):
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
    rol= models.ForeignKey(Rol)
    usuario=models.ForeignKey(User)
    proyecto=models.ForeignKey(Proyectos)

    class Meta:
            unique_together = ('rol', 'usuario', 'proyecto')
        #    permissions=(("asociarRol","puede asociar roles a usuarios"),)

class lineaBase(models.Model):

    E_ABIERTA='ABIERTA'
    E_CERRADA='CERRADA'
    E_ROTA='ROTA'
    E_REVISION='REVISION'
    ESTADO_CHOICES=(
        ('ABIERTA','Abierta'),
        ('CERRADA', 'Cerrada'),
        ('ROTA','Rota'),
        ('REVISION','En_Revision'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=E_ABIERTA, null=False,blank= False)
    fase= models.ForeignKey(Fases1,null=True, blank= True)

    def __unicode__(self):
         return self.estado



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
    lb= models.ForeignKey(lineaBase, null=True, blank= True)
    solicitudAprobada=models.BooleanField(default=0)
    revocar=models.DateField(null=True, blank= True, default='1000-01-01')

    antecesorHorizontal= models.ForeignKey('self',related_name='RantecesorHorizontal',null=True, blank= True)
    sucesorHorizontal= models.ForeignKey('self',related_name='RsucesorHorizontal',null=True, blank= True)
    sucesorVertical= models.ForeignKey('self',related_name='RsucesorVertical',null=True, blank= True)
    antecesorVertical=models.ForeignKey('self',related_name='RantecesorVertical',null=True, blank=True)
    relacion= models.CharField(max_length=20, choices= ESTADOS_RELACION, null=True, blank=True)

    def __unicode__(self):
         return self.nombre

        #class Meta:
        #    permissions=(("asociarRol","puede asociar roles a usuarios"),)


class Archivo(models.Model):
    archivo=models.FileField(upload_to='archivos')
    item=models.ForeignKey(Item, null=True)
    nombre=models.CharField(max_length=100, null=True)



class SolicitudCambio(models.Model):
    E_ESPERA= 'EN_ESPERA'
    E_APROBADA= 'APROBADA'
    E_RECHAZADA= 'RECHAZADA'
    ESTADOS= (
        (E_ESPERA, 'En_espera'),
        (E_APROBADA, 'Aprobada'),
        (E_RECHAZADA, 'Rechazada'),
    )

    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    descripcion=models.TextField(max_length=140, verbose_name='Descripcion')
    proyecto=models.ForeignKey(Proyectos)
    item=models.ForeignKey(Item)
    fecha=models.DateField(auto_now= True, verbose_name='Fecha')
    costo=models.PositiveIntegerField(verbose_name='Costo')
    usuario=models.ForeignKey(User)
    estado=models.CharField(max_length=10, verbose_name='Estado',choices=ESTADOS, default=E_ESPERA)
    cantidadDias=models.IntegerField()

class Voto(models.Model):
    V_APROBADO= 'APROBADO'
    V_RECHACZADO= 'RECHAZADO'
    VOTOS= (
        (V_APROBADO, 'A_favor'),
        (V_RECHACZADO, 'En_contra'),
    )
    solicitud=models.ForeignKey(SolicitudCambio)
    usuario=models.ForeignKey(User)
    voto=models.CharField(max_length=10, verbose_name='Voto',choices=VOTOS, null=False)


