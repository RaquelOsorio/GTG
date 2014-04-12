from unittest import TestCase
from models import inicio_sesion
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY

__author__ = 'sonia'

class TestInicio_sesion(TestCase):
    def setUp(self):
        """Test para las pruebas unitarias.
         Innicio sesion
         import: importa los modulos necesarios
        """
        self.client = Client()
        self.username = 'testusr'
        self.email = 'test@test.com'
        self.password = 'testpw'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

    def test_inicio_sesion_exitoso(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
