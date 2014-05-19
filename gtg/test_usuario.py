__author__ = 'sonia'
import unittest
from django.contrib.auth import SESSION_KEY
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
class GTGTestCase(TestCase):

    def test_crear_usuario(self):
        '''
        Test para la creacion de un usuario con contrasenha
        '''
        u = User.objects.create_user('testuser', 'test@example.com', 'testpw')
        self.assertTrue(u.has_usable_password())
        self.assertFalse(u.check_password('bad'))
        self.assertTrue(u.check_password('testpw'))

        # Test para contrasenha incorrecta
        u.set_unusable_password()
        u.save()
        self.assertFalse(u.check_password('testpw'))
        self.assertFalse(u.has_usable_password())
        u.set_password('testpw')
        self.assertTrue(u.check_password('testpw'))
        u.set_password(None)
        self.assertFalse(u.has_usable_password())

        # Test para identificar permisos
        self.assertTrue(u.is_authenticated())
        self.assertFalse(u.is_staff)
        self.assertTrue(u.is_active)
        self.assertFalse(u.is_superuser)

        # Test para creacion sin password
        u2 = User.objects.create_user('testuser2', 'test2@example.com')
        self.assertFalse(u2.has_usable_password())
def test_inicio(self):
    '''
    Test para ver si puede entrar a la pagina de inicio
    '''

    def test_modificar_usuarios(self):
        '''
        Test para cambiar el estado de un usuario
        '''
        usuario2 = User.objects.create_user('testuser33', 'test@example.com', 'testpw')
        usuario2.is_active=False
        resp = self.client.get('/usuario/editarUsuario/6?')
        self.assertEqual(resp.status_code, 301)

        self.assertEqual([usuario2.is_active for user in resp.context['datos']], [False])

    def logout(self):
        '''
        Test para el logout
        '''
        response = self.client.get('/cerrar/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(SESSION_KEY not in self.client.session)
