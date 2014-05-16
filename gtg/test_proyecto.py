from django.test import TestCase
from django.contrib.auth.models import User
from gtg.models import Proyectos
from django.test import Client

class GTGTestCase(TestCase):
    def test_crear_proyecto(self):
        '''
        test para comprobar que se crea un item
        '''

        c = Client()
        c.login(username='vivi', password='vivi')
        print('\n------Ejecutando test para registrar un proyecto-------\n')

