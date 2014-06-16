__author__ = 'sonia'
#! /usr/bin/python

from django.contrib.auth.forms import User
from gtg.models import Proyectos
from gtg.models import Fases1
from gtg.models import TipoItem
from gtg.models import TipoAtributo
from gtg.models import lineaBase
from gtg.models import Item
from gtg.models import Rol
from gtg.models import Voto
from gtg.models import SolicitudCambio
import os, datetime
from gtg.models import lineaBase


#Se vacian las tablas
def vaciar():
    Proyectos.objects.all().delete()
    Fases1.objects.all().delete()
    TipoItem.objects.all().delete()
    TipoAtributo.objects.all().delete()
    lineaBase.objects.all().delete()
    Item.objects.all().delete()
    Rol.objects.all().delete()
    SolicitudCambio.objects.all().delete()
    User.objects.all().delete()

#ejecutar asi ./manage.py shell < cargardb.py
def cargarUsuario():

   """Script de carga de Usuarios al sistema"""
   usuario2 = User.objects.create_user(username='vivi', password='vivi')
   usuario3 = User.objects.create_user(username='pepe', password='pepe')
   usuario4 = User.objects.create_user(username='ana', password='ana')
   usuario5 = User.objects.create_user(username='hugo', password='hugo')


def cargarProyecto():
    """
        Script de carga de proyecto para el sistema.
    """
    proyecto1 = Proyectos.objects.create_proyecto(nombre='lpm', fechaInicio = '22/05/2014', fechaFin= '22/05/2015', complejidad=1, estado= 'PEN', lider_id=1)
    proyecto2 = Proyectos.objects.create_proyecto(nombre='gtg', fechaInicio = '22/05/2014', fechaFin= '22/05/2015', complejidad=1, estado= 'ACT', lider=User.usuario3)
    proyecto3 = Proyectos.objects.create_proyecto(nombre='gestograma', fechaInicio = '22/05/2014', fechaFin= '22/05/2015', complejidad=1, estado= 'ANU', lider=User.usuario4)
    proyecto4 = Proyectos.objects.create_proyecto(nombre='alfa', fechaInicio = '22/05/2014', fechaFin= '22/05/2015', complejidad=1, estado= 'FIN', lider=User.usuario4)
    proyecto5 = Proyectos.objects.create_proyecto(nombre='project', fechaInicio = '22/05/2014', fechaFin= '22/05/2015', complejidad=1, estado= 'PEN', lider=User.usuario2)



def cargarFases():
    """
    Script de carga de fase para proyectos del sistema
    """
    fase1 = Fases1.objects.create_fase(fechaInicio = '22/05/2014', fechaFin= '22/05/2015', nombre='fase1', descripcion='primera fase ', estado= 'PEN', proyecto=Proyectos.proyecto1)
    fase2 = Fases1.objects.create_fase(fechaInicio = '22/05/2014', fechaFin= '22/05/2015', nombre='fase2', descripcion='segunda fase',estado= 'INA', proyecto=Proyectos.proyecto1)
    fase3 = Fases1.objects.create_fase(fechaInicio = '22/05/2014', fechaFin= '22/05/2015', nombre='fase3', descripcion='tercera fase',estado= 'ACT', proyecto=Proyectos.proyecto1)
    fase4 = Fases1.objects.create_fase(fechaInicio = '22/05/2014', fechaFin= '22/05/2015', nombre='fase4', descripcion='cuarta fase', estado= 'PEN',proyecto=Proyectos.proyecto1)
    fase5 = Fases1.objects.create_fase(fechaInicio = '22/05/2014', fechaFin= '22/05/2015', nombre='fase5', descripcion='quinta fase', estado= 'FIN', proyecto=Proyectos.proyecto1)


def cargarAtributo():

    tipoAtributo1= TipoAtributo.objects.create_atributo(nombre = 'atributo1', descripcion='describe atributo1')
    tipoAtributo2= TipoAtributo.objects.create_atributo(nombre = 'atributo2', descripcion='describe atributo2')
    tipoAtributo3= TipoAtributo.objects.create_atributo(nombre = 'atributo3', descripcion='describe atributo3')
    tipoAtributo4= TipoAtributo.objects.create_atributo(nombre = 'atributo4', descripcion='describe atributo4')
    tipoAtributo5= TipoAtributo.objects.create_atributo(nombre = 'atributo5', descripcion='describe atributo5')


def cargarTipoItem():


    tipo1= TipoItem.objects.create_tipoItem(nombre='tipo1',descripcion='representa un tipo1',tipoAtributo= TipoAtributo.tipoAtributo1)
    tipo2= TipoItem.objects.create_tipoItem(nombre='tipo2',descripcion='representa un tipo2',tipoAtributo= TipoAtributo.tipoAtributo1)
    tipo3= TipoItem.objects.create_tipoItem(nombre='tipo3',descripcion='representa un tipo3',tipoAtributo= TipoAtributo.tipoAtributo1)
    tipo4= TipoItem.objects.create_tipoItem(nombre='tipo4',descripcion='representa un tipo4',tipoAtributo= TipoAtributo.tipoAtributo1)
    tipo5= TipoItem.objects.create_tipoItem(nombre='tipo5',descripcion='representa un tipo5',tipoAtributo= TipoAtributo.tipoAtributo1)

def cargarlb():
    lb1= lineaBase.objects.create_lb(estado= 'ABIERTA', fase=Fases1.fase5)


def cargarItem():
    item1= Item.objects.create_item(nombre='item1', prioridad=1, estado= 'REDAC', descripcion='describe el item1', tipoItem=TipoItem.tipo1, fase=Fases1.fase1)
    item2= Item.objects.create_item(nombre='item2', prioridad=1, estado= 'VAL', descripcion='describe el item2', tipoItem=TipoItem.tipo1, fase=Fases1.fase5, lb=lineaBase.lb1)
    item3= Item.objects.create_item(nombre='item3', prioridad=1, estado= 'VAL', descripcion='describe el item3', tipoItem=TipoItem.tipo1, fase=Fases1.fase5, lb=lineaBase.lb1, antecesorVertical= Item.item2)
    item4= Item.objects.create_item(nombre='item4', prioridad=1, estado= 'TER', descripcion='describe el item4', tipoItem=TipoItem.tipo1, fase=Fases1.fase1, antecesorHorizontal= Item.item2)
    item5= Item.objects.create_item(nombre='item5', prioridad=1, estado= 'DESAC', descripcion='describe el item5', tipoItem=TipoItem.tipo1, fase=Fases1.fase1)




def cargarSolicitud():

    solicitud1= SolicitudCambio.objects.create_solicitud(nombre= 'solicitud1', descripcion='indica el motivo de la solicitud1', proyecto=Proyectos.proyecto1, item=Item.item1, costo=2, usuario= User.usuario2)
    solicitud2= SolicitudCambio.objects.create_solicitud(nombre= 'solicitud2', descripcion='indica el motivo de la solicitud2', proyecto=Proyectos.proyecto1, item=Item.item2, costo=2, usuario= User.usuario2)
    solicitud3= SolicitudCambio.objects.create_solicitud(nombre= 'solicitud3', descripcion='indica el motivo de la solicitud3', proyecto=Proyectos.proyecto1, item=Item.item3, costo=2, usuario= User.usuario2)

"""Empieza la ejecucion"""
if __name__ == '__main__':
    print ("Cargando datos en la base de datos...")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestograma.settings")
    cargarUsuario()
    cargarProyecto()
    cargarFases()
    cargarAtributo()
    cargarTipoItem()
    cargarItem()
    cargarSolicitud()
