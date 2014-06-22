__author__ = 'viviana'

import unittest
from django.test import TestCase
from gtg.models import Fases1
from django.contrib.auth.models import User
from django.test import Client

class GTGTestCase(TestCase):

    fixtures = ["items_testmaker"]
    print('\n------Ejecutando test para ingresar al sistema-------')

    def test_abrir_proyecto(self):
        '''
        test para comprobar que se listan los pryectos de un usuario especifico
        '''
        c = Client()
        c.login(username='vivi', password='vivi')

        resp = c.get('/proyecto/')
        a=self.assertEqual(resp.status_code, 200)

        print ('Lista de proyectos existentes')

    def test_abrir_fase(self):
        '''
        test para comprobar que se abren las fases de un proyecto y usuarios especificos
        '''
        c = Client()
        c.login(username='vivi', password='vivi')

        resp = c.get('/fase1/500')
        self.assertTrue(resp.status_code, 404)

        print ('Test listar fases de proyecto inexistente')

        resp = c.get('/fase1/1')
        self.assertTrue(resp.status_code, 200)
        print ('Test listar fases de proyecto existente')



    def test_crear_fase(self):
        '''
        test para comprobar que se crea un item
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para registrar una fase-------\n')

        resp = c.get('/fase1/registrarFase/132')
        self.assertTrue(resp.status_code, 404)
        print ('\n1 Test acceder a crear fase en un proyecto inexistente')

        resp = c.get('/fase1/registrarFase/1')
        self.assertTrue(resp.status_code, 200)
        print ('\n2 Test acceder a crear fase en un proyecto existente')

        resp = c.post('/fase1/registrarFase/1',{'nombre':'fase1'})
        self.assertTrue(resp.status_code,302)
        print ('\n3 No crea la fase si no completa todos los campos')

        resp = c.post('/fase1/registrarFase/1',{'nombre':'fase1', 'descripcion':'KKKK','estado':'1'})
        self.assertEqual(resp.status_code,301)
        print ('\n4 No crea la fase si un campo esta mal completado')

        resp = c.post('/fase1/registrarFase/1',{"fechaMod": "2014-05-16", "proyectos": 1, "fechaInicio": "2014-05-07", "descripcion": "KKKK", "nombre": "fase1", "estado": "INA", "fechaFin": "2015-05-07"})
        self.assertTrue(resp.status_code,200)
        print ('\n5 Crea la fase si esta correctamente completado\n')

    def test_modificar_fae(self):
        '''
        test para comprobar que se crea un item hijo
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para modificar fase-------\n')

        resp = c.get('/fase/editarFase/45')
        self.assertTrue(resp.status_code, 404)

        print ('Test acceder modificar fase inexistente')

        resp = c.get('/fase/editarFase/1')
        self.assertTrue(resp.status_code, 404)
        print ('Test acceder a modificar fase existente')

        resp = c.post('/fase/editarFase/1',{'nombre':'fase11'})
        self.assertTrue(resp.status_code,200)
        print ('Modifica la fase\n')


    def test_eliminar_item(self):

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para eliminar fase-------\n')
        resp = c.get('/fase/eliminar_fase/88')
        self.assertEqual(resp.status_code, 301)
        print ('Test eliminar fase que no existe')

        resp = c.get('/fase/eliminar_fase/1')
        self.assertTrue(resp.status_code, 200)
        print( 'Test eliminar fase que existe\n')
