from django.test import TestCase
from django.contrib.auth.models import User
from gtg.models import Proyectos
from gtg.models import SolicitudCambio
from gtg.models import Item
from django.test import Client

class GTGTestCase(TestCase):

    fixtures = ["items_testmaker"]

    def test_incluir_comite(self):
        '''
        test para comprobar que se asignan miembros al comite de cambios
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para incluir miembros al cambio-------\n')

        resp = c.post('/incluir_al_Comite/44/44')
        self.assertTrue(resp.status_code, 404)
        print ('Test para incluir al comite un usuario inexistente a un proyecto inexistente')

        resp = c.post('/incluir_al_Comite/2/')
        self.assertEqual(resp.status_code,200)
        print ('\n1 Incluye un nuevo o varios miembros al comite de cambios')
