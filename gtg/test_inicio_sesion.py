from unittest import TestCase

from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY

__author__ = 'sonia'

class TestInicio_sesion(TestCase):
    def setUp(self):
<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d
        """Test para las pruebas unitarias.
         Inicio sesion
         import: importa los modulos necesarios
        """
        self.client = Client()
        self.username = 'trtr'
        self.email = 'test@tesm'
        self.password = 'stpw'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

<<<<<<< HEAD
    def test_inicio_sesion_exitoso(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

        """Test para las pruebas unitarias.inicio sesion """
        self.Client = Client()
        self.username = 'tt'
        self.email = 'test@test.com'
        self.password = 'pw'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

=======
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
    def test_inicio_sesion_exitoso(self, password='pw'):
        login = self.Client.login(username=self.username, password=password)
        self.assertEqual(login, True)

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
>>>>>>> 422ad2cad28d48cc948a7890ed3910fb77c281e1
>>>>>>> 64570d5fc03175bcdd7814fba88c89225e9a231d
