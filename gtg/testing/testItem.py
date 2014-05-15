__author__ = 'viviana'

import unittest
from django.test import TestCase
from gtg.models import Fases1
from django.contrib.auth.models import User
from django.test import Client

class Test_crear_fase(TestCase):
    def test_crear_item(self):
        '''
        test para comprobar que se crea un item
        '''

        c = Client()
        c.login(username='vivi', password='vivi')

        resp = c.get('/gtg/registrarItem/22')
        self.assertEqual(resp.status_code, 404)

        print ('\n1 Test acceder a crear item en una fase inexistente')

        resp = c.get('/gtg/registrarItem/2')
        self.assertEqual(resp.status_code, 404)

        print ('\n2 Test acceder a crear item en una fase existente')

        resp = c.post('/gtg/registrarItem/2',{'nombre':'Item1'})
        self.assertEqual(resp.status_code,200)
        print ('\n3 No crea el item si no completa todos los campos')

        resp = c.post('/gtg/registrarItem/2',{'nombre':'Item1', 'descripcion':'dsdd','prioridad':'1'})
        self.assertEqual(resp.status_code,200)
        print ('\n4 No crea el item si un campo esta mal completado')

        resp = c.post('/gtg/registrarItem/3',{"pk": 1, "model": "gtg.item", "lb": 1, "tipoItem": 1, "version": 1, "descripcion": "jkjk", "nombre": "Item1", "fechaModi": "2014-05-14", "estado": "VAL", "prioridad": 1, "fase": 1})
        self.assertEqual(resp.status_code,200)
        print ('\n5 Crea el item si esta correctamente completado')
