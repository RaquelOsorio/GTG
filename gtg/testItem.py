__author__ = 'viviana'

import unittest
from django.test import TestCase
from gtg.models import Fases1
from django.contrib.auth.models import User
from django.test import Client

class GTGTestCase(TestCase):


    def test_crear_item(self):
        '''
        test para comprobar que se crea un item
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para registrar un item-------\n')

        resp = c.get('/item/registrarItem/132')
        self.assertEqual(resp.status_code, 301)

        print ('\n1 Test acceder a crear item en una fase inexistente')

        resp = c.get('/item/registrarItem/1')
        self.assertEqual(resp.status_code, 301)

        print ('\n2 Test acceder a crear item en una fase existente')

        resp = c.post('/item/registrarItem/1',{'nombre':'Item1'})
        self.assertEqual(resp.status_code,301)
        print ('\n3 No crea el item si no completa todos los campos')

        resp = c.post('/item/registrarItem/1',{'nombre':'Item1', 'descripcion':'dsdd','prioridad':'asas'})
        self.assertEqual(resp.status_code,301)
        print ('\n4 No crea el item si un campo esta mal completado')

        resp = c.post('item/registrarItem/1',{ "pk": 1, "lb": 1, "tipoItem": 1, "version": 1, "descripcion": "dsds", "nombre": "Item1", "fechaModi": "2014-05-15", "estado": "VAL", "prioridad": 1, "fase": 1})
        self.assertTrue(resp.status_code,200)
        print ('\n5 Crea el item si esta correctamente completado\n')

    def test_modificar_item(self):
        '''
        test para comprobar que se crea un item hijo
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para modificar item-------\n')

        resp = c.get('/item/modificarItem/45')
        self.assertEqual(resp.status_code, 301)

        print ('Test acceder modificar item inexistente')

        resp = c.get('/item/modificarItem/1')
        self.assertEqual(resp.status_code, 301)
        print ('Test acceder a modificar item existente')

        resp = c.post('/item/modificarItem/1',{'nombre':'Item'})
        self.assertEqual(resp.status_code,301)
        print ('Modifica el item\n')


    def test_eliminar_item(self):
        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para eliminar item-------\n')
        resp = c.get('/eliItem/88')
        self.assertEqual(resp.status_code, 301)
        print ('Test eliminar item que no existe')
        resp = c.get('/eliItem/1')
        self.assertEqual(resp.status_code, 301)
        print( 'Test eliminar item que existe\n')

