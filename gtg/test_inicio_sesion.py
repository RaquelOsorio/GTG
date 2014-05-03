from unittest import TestCase

from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY

__author__ = 'sonia'

class TestInicio_sesion(TestCase):
    def setUp(self):

        """Test para las pruebas unitarias.
         Inicio sesion
         import: importa los modulos necesarios
        """
        self.client = Client()
        self.username = 'trtr'
        self.email = 'test@tesm'
        self.password = 'stpw'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

    def test_inicio_sesion_exitoso(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

        """Test para las pruebas unitarias.inicio sesion """
        self.Client = Client()
        self.username = 'tt'
        self.email = 'test@test.com'
        self.password = 'pw'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

    def test_inicio_sesion_exitoso(self, password='pw'):
        login = self.Client.login(username=self.username, password=password)
        self.assertEqual(login, True)

