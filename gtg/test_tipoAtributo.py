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
        c.login(username='vivi', password='vivi')
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

    def test_modificar_tipoAtributo(self):
        '''
        test para comprobar que se modifica un tipo de atributo
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para modificar tipo de atributo-------\n')

        resp = c.get('/tipoAtributo/modificar_tipoAtributo/45')
        self.assertTrue(resp.status_code, 404)

        print ('Test acceder modificar tipo de atributo inexistente')

        resp = c.get('tipoAtributo/modificar_tipoAtributo/1')
        self.assertTrue(resp.status_code, 302)
        print ('Test acceder a modificar tipo atributo existente')

        resp = c.post('/tipoAtributo/modificar_tipoAtributo/1',{'nombre':'Atributo11'})
        self.assertTrue(resp.status_code,200)
        print ('Modifica el tipo de atributo\n')


    def test_eliminar_item(self):
        '''
        test para comprobar que se elimina un tipo de atributo
        '''
        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para eliminar tipo de atributo-------\n')
        resp = c.get('/eliTipoAtributo/88')
        self.assertEqual(resp.status_code, 301)
        print ('Test eliminar tipo de atributo que no existe')

        resp = c.get('/eliTipoAtributo/1')
        self.assertTrue(resp.status_code, 200)
        print( 'Test eliminar tipo de atributo que existe\n')
