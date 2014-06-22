from django.test import TestCase
from django.contrib.auth.models import User
from gtg.models import Proyectos
from gtg.models import SolicitudCambio
from gtg.models import Item
from django.test import Client

class GTGTestCase(TestCase):

    fixtures = ["items_testmaker"]

    def test_crear_solicitudCambio(self):
        '''
        test para comprobar que se crea una solicitud
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para crear Solicitud de cambio-------\n')

        resp = c.post('/itemFase/crearSolicitudCambio/44')
        self.assertTrue(resp.status_code, 404)
        print ('Test para crear solicitud con un item inexistente')

        resp = c.post('/itemFase/crearSolicitudCambio/3',{ "usuario": 2, "fecha": "2014-05-23", "costo": 0, "item": 3, "proyecto": 2, "estado": "EN_ESPERA"})
        self.assertTrue(resp.status_code,302)
        print ('\n1 No crea la solicitud si no completa todos los campos')

        resp = c.post('/itemFase/crearSolicitudCambio/3',{ "usuario": 2, "fecha": "2014-05-23", "costo": 'asasasas', "item": 3, "proyecto": 2, "descripcion": "asasas", "nombre": "solicitud3", "estado": "EN_ESPERA"})
        self.assertEqual(resp.status_code,301)
        print ('\n2 No crea la solicitud si un campo esta mal completado')

        resp = c.post('/itemFase/crearSolicitudCambio/3',{ "usuario": 2, "fecha": "2014-05-23", "costo": 0, "item": 3, "proyecto": 2, "descripcion": "asasas", "nombre": "solicitud3", "estado": "EN_ESPERA"})
        self.assertTrue(resp.status_code,200)
        print ('\n3 Crea la solicitud si esta correctamente completado\n')

    def test_estudiarSolicitud(self):
        '''
        test para comprobar el estado de una solicitud
        '''
        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para verificar Solicitud de cambio-------\n')

        resp = c.post('/listaSolicitudes/')
        self.assertEqual(resp.status_code, 200)
        print ('Test para listar solicitudes')

        resp = c.post('/listaSolicitudes/votar/33')
        self.assertTrue(resp.status_code,404)
        print ('\n1 Test para votar por una solicitud inexistente')

        resp = c.post('/listaSolicitudes/votar/3/')
        self.assertEqual(resp.status_code,200)
        print ('\n1 Test para votar por una solicitud existente')

        resp = c.post('/listaSolicitudes/votar/1/', {"voto": "APROBADO", "usuario": 2, "solicitud": 1})
        self.assertTrue(resp.status_code,200)
        print ('\n1 Test para votar por una solicitud existente y aprobarla')

