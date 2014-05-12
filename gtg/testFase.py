__author__ = 'viviana'

import unittest
from django.test import TestCase
from gtg.models import Fases1
from django.contrib.auth.models import User

class Test_crear_fase(TestCase):
    def test_crear_fase(self):
        '''
        Test para la creacion de una fase
        '''
        u = User.objects.create_user('testuser', 'test@example.com', 'testpw')
        self.assertTrue(u.has_usable_password())
        self.assertFalse(u.check_password('ck'))
        self.assertTrue(u.check_password('testphjw'))
        print("Registro exitoso de usuario :)")

        # Test para contrasena incorrecta
        u.set_unusable_password()
        u.save()
        self.assertFalse(u.check_password('testpw'))
        self.assertFalse(u.has_usable_password())
        u.set_password('testpw')
        self.assertTrue(u.check_password('testpw'))
        u.set_password(None)
        self.assertFalse(u.has_usable_password())
        if u.set_password(None)==True:
            print("contrasena incorrecta")

