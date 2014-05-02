__author__ = 'sonia'
import unittest
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User

class Test_modificar_usuario(TestCase):
    def test_detalle_usuarios(self):
        '''
        Test para modificar usuario de un usuario
        '''
        usuario2 = User.objects.create_user('testuser33', 'test@example.com', 'testpw')
        usuario1= usuario2
        usuario2.is_active=True
        usuario2.username= 'testuser33'
        usuario2.email= 'test@example.com'
        usuario2.passward= 'pw'
        resp = self.client.get('lista_usuarios/editarUsuario/2/?')
        self.assertEqual(resp.status_code, 404)
        if self.assertEqual(usuario1.username, usuario2.username):
            print("no se ha modificado ningun atributo")
        else:
            print("usuario modificado ;)")

    def test_delete(self):
        usuario2 = User.objects.create_user('testuser33', 'test@example.com', 'testpw')
        if self.assertFalse(usuario2.delete()):
            print("no se pudo eliminar el usuario, verifique si el usuario esta registrado")
        else:
            print("usuario eliminado")



