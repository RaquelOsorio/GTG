from django.test import TestCase
from django.contrib.auth.models import User
from gtg.models import Proyectos
from django.test import Client

class GTGTestCase(TestCase):

    fixtures = ["items_testmaker"]

    def test_crear_tipoAtributo(self):
        '''
        test para comprobar que se crea un tipo de atributo
        '''

        c = Client()
        c.login(username='sonia', password='sonia')
        print('\n------Ejecutando test para registrar un tipo de atributo-------\n')

        resp = c.post('/tipoAtributo/registrarTipoAtributo',{'nombre':'Atributo1'})
        self.assertTrue(resp.status_code,302)
        print ('\n1 No crea el tipo de atributo si no completa todos los campos')

        resp = c.post('/tipoAtributo/registrarTipoAtributo',{"descripcion": "1", "nombre": "Atributo1", "tipo": "Entero"})
        self.assertEqual(resp.status_code,301)
        print ('\n2 No crea el tipo de atributo si un campo esta mal completado')

        resp = c.post('/tipoAtributo/registrarTipoAtributo',{"descripcion": "kll", "nombre": "Atributo1", "tipo": "Entero"})
        self.assertTrue(resp.status_code,200)
        print ('\n3 Crea el tipo de atributo si esta correctamente completado\n')


    def test_crear_tipoItem(self):
        '''
        test para comprobar que se crea un tipo de item
        '''

        c = Client()
        c.login(username='sonia', password='sonia')
        print('\n------Ejecutando test para registrar un tipo de item-------\n')

        resp = c.post('/tipoItem/registrarTipoItem',{'nombre':'tipo1'})
        self.assertTrue(resp.status_code,302)
        print ('\n1 No crea el tipo de item si no completa todos los campos')

        resp = c.post('/tipoItem/registrarTipoItem',{ "descripcion": 1,
        "nombre": "tipo1",
        "tipoAtributo": 1})
        self.assertEqual(resp.status_code,301)
        print ('\n2 No crea el tipo de item si un campo esta mal completado')

        resp = c.post('/tipoItem/registrarTipoItem',{ "descripcion": "tipo1",
        "nombre": "tipo1",
        "tipoAtributo": 1})
        self.assertTrue(resp.status_code,200)
        print ('\n3 Crea el tipo de item si esta correctamente completado\n')

