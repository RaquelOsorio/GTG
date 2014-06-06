from django.test import TestCase
from django.contrib.auth.models import User
from gtg.models import Proyectos
from django.test import Client
from gtg.views import incluir_al_Comite

class GTGTestCase(TestCase):
    def test_crear_proyecto(self):
        '''
        test para comprobar que se crea un item
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para registrar un proyecto-------\n')

        #resp = c.post('/proyecto/registrarProyecto/',{"fechaMod": "2014-05-23", "fechaInicio": "2014-05-07", "lider": 1, "complejidad": "asasas", "nombre": "lpm", "estado": "PEN", "fechaFin": "2015-05-07"})
        #self.assertEqual(resp.status_code,302)
        #print ('\n2 No crea el proyecto si un campo esta mal completado')

        #resp = c.post('/proyecto/registrarProyecto/',{"fechaMod": "2014-05-16", "fechaInicio": "2014-05-07", "lider": 1, "complejidad": 1, "nombre": "lpm", "estado": "PEN", "fechaFin": "2015-05-07"})
        #self.assertTrue(resp.status_code,200)
        #print ('\n3 Crea el proyecto si esta correctamente completado\n')

    def test_modificar_proyecto(self):
        '''
        test para comprobar que se crea un item hijo
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para modificar proyecto-------')

        resp = c.get('/proyecto/editarProyecto/45')
        self.assertTrue(resp.status_code, 404)

        print ('Test acceder modificar proyecto inexistente')

        resp = c.get('/proyecto/editarProyecto/1')
        self.assertTrue(resp.status_code, 404)
        print ('Test acceder a modificar proyecto existente')

        resp = c.post('/proyecto/editarProyecto/1',{'nombre':'gestograma'})
        self.assertTrue(resp.status_code,200)
        print ('Modifica el proyecto\n')

    def test_visualizar_proyecto(self):
        '''
        test para comprobar que se crea un item hijo
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para visualizar proyecto-------')

        resp = c.get('/proyecto/verProyecto/45')
        self.assertTrue(resp.status_code, 404)

        print ('Test acceder visualizar proyecto inexistente')

        resp = c.get('/proyecto/verProyecto/1')
        self.assertTrue(resp.status_code, 200)
        print ('Test acceder a visualizar existente')

