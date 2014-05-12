__author__ = 'sonia'
#from django.test import TestCase
from django.utils import unittest
from gtg.models import Proyectos
from django.contrib.auth.models import User

class TestProyectoView(unittest.TestCase):
    def crear_usuario(self, username, password='vivi'):
        return User.objects.create(username=username, password=password)

    def crear_proyecto(self,nombre):
        w= self.crear_usuario(username='liderU')
        p= Proyectos.objects.create(nombre= nombre, descripcion= 'testing para proyecto', lider= w)
        return (p)

    def test_crear_proyecto(self):
        u= self.crear_proyecto(nombre= 'gtg')
        self.assertTrue(isintance(u, Proyectos))
        self.assertEqual(u.__unicode__(), u.nombre)
        print ("Ejecutando testing para crear proyecto")