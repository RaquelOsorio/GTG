__author__ = 'viviana'

import unittest
from django.test import TestCase
from gtg.models import Fases1
from django.contrib.auth.models import User
from django.test import Client

class GTGTestCase(TestCase):

    fixtures = ["items_testmaker"]

    print('\n------Ejecutando test para Linea Base-------')

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

    def test_abrir_lb(self):
        '''
        test para comprobar que se abren las fases de un proyecto y usuarios especificos
        '''
        c = Client()
        c.login(username='vivi', password='vivi')

        resp = c.get('/lb/500')
        self.assertTrue(resp.status_code, 404)

        print ('Test listar lb de fase inexistente')

        resp = c.get('/lb/1')
        self.assertTrue(resp.status_code, 200)
        print ('Test listar lb de fases existente')


    def test_crear_lb(self):
        '''
        test para comprobar que se genera la linea base
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para generar linea base-------\n')

        resp = c.get('/lb/generarlb/132')
        self.assertTrue(resp.status_code, 404)
        print ('\n1 Test acceder a generar lb en una fase inexistente')

        resp = c.get('/lb/generarlb/1')
        self.assertTrue(resp.status_code, 200)
        print ('\n2 Test acceder a generar lb en una fase existente')

        resp = c.post('/lb/generarlb/1',{})
        print ('\n3 Se genera la lb si esta correctamente completado\n')

    def test_relacionar_itemLb(self):
        '''
        test para comprobar que se crea un item hijo
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para relacionar item a la linea base-------\n')

        resp = c.get('/lb/listaItemsTer/45')
        self.assertTrue(resp.status_code, 404)

        print ('Test listar items en estado terminado en una fase inexistente')

        resp = c.get('/lb/listaItemsTer/1/')
        self.assertTrue(resp.status_code, 200)
        print ('Test listar items en estado terminado en una fase existente')

        resp = c.post('/listaItemsTer/relacionarItemLb/1',{})
        self.assertTrue(resp.status_code,200)
        print ('Relaciona el item a la linea base\n')


    def test_eliminar_item(self):

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para eliminar item-------\n')
        resp = c.get('/eliItem/88')
        self.assertEqual(resp.status_code, 301)
        print ('Test eliminar item que no existe')

        resp = c.get('/eliItem/1')
        self.assertTrue(resp.status_code, 200)
        print( 'Test eliminar item que existe\n')

    def test_revivir_item(self):

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para revivir item-------\n')

        resp = c.get('/item/revivirItem/88')
        self.assertEqual(resp.status_code, 301)
        print ('Test revivir item que no existe')

        resp = c.get('/item/revivirItem/1')
        self.assertTrue(resp.status_code, 200)
        print( 'Test revivir item que existe\n')

    def test_reversionar(self):
        '''
        test para comprobar que se reversiona un item
        '''

        c = Client()
        c.login(username='vivi', password='vivi')

        resp = c.get('/item/reversionarItem/45')
        self.assertTrue(resp.status_code, 404)

        print ('Test acceder reversionar item inexistente')

        resp = c.get('/item/reversionarItem/2')
        self.assertTrue(resp.status_code, 200)
        print ('Test acceder a reversionar item existente')

        resp = c.post('/item/reversionarItem/2', {'version':1})
        self.assertTrue(resp.status_code,200)
        print ('Reversiona el item')

