# coding: utf-8
import os
import unittest
from random import randint
from pontopass import Pontopass
from pontopass.utils import Object
from pontopass import exceptions


PONTOPASS_API_USER = os.getenv('PONTOPASS_API_USER')
PONTOPASS_API_PASSWORD = os.getenv('PONTOPASS_API_PASSWORD')


class ClientTestCase(unittest.TestCase):

    users_to_remove = []

    @classmethod
    def setUpClass(cls):
        cls.pontopass = Pontopass(
            api_user=PONTOPASS_API_USER,
            api_pass=PONTOPASS_API_PASSWORD,
        )

    @classmethod
    def tearDownClass(cls):
        for user in cls.users_to_remove:
            device_list = cls.pontopass.user(user).device.list()

            for device in device_list:
                cls.pontopass.user(user).device.delete(device.id)

            cls.pontopass.user.delete(user=user)

    def test_add_valid_user(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))
        name = u'Vinícius Cainelli'

        response = self.pontopass.user.add(user=user, name=name)

        self.assertTrue(response.id)
        self.assertTrue(isinstance(response, Object))

        self.users_to_remove.append(user)

    def test_add_user_already_exists(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))
        name = u'Vinícius Cainelli'

        response = self.pontopass.user.add(user=user, name=name)

        self.assertTrue(response.id)
        self.assertTrue(isinstance(response, Object))

        self.users_to_remove.append(user)

        with self.assertRaises(exceptions.UserAlreadyExists):
            self.pontopass.user.add(user=user, name=name)

    def test_delete_valid_user(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))
        name = u'Vinícius Cainelli'

        response_add = self.pontopass.user.add(user=user, name=name)

        self.assertTrue(response_add.id)
        self.assertTrue(isinstance(response_add, Object))

        response_delete = self.pontopass.user.delete(user=user)

        self.assertTrue(response_delete)

    def test_delete_invalid_user(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))

        with self.assertRaises(exceptions.UserDoesNotExist):
            self.pontopass.user.delete(user=user)

    def test_add_device(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))
        name = u'Vinícius Cainelli'

        response = self.pontopass.user.add(user=user, name=name)

        self.assertTrue(response.id)
        self.assertTrue(isinstance(response, Object))

        self.users_to_remove.append(user)

        response2 = self.pontopass.user(user).device.add(Pontopass.SMS, '1681813981', 'iphone')

        self.assertTrue(response2.method_id)
        self.assertTrue(isinstance(response2, Object))
        self.assertEqual(response2.status, 0)

    def test_list_devices(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))
        name = u'Vinícius Cainelli'
        mobile_namber = randint(10000000000, 99999999999)

        response = self.pontopass.user.add(user=user, name=name)

        self.assertTrue(response.id)
        self.assertTrue(isinstance(response, Object))

        self.users_to_remove.append(user)

        response2 = self.pontopass.user(user).device.add(Pontopass.SMS, mobile_namber, 'desc_{0}'.format(randint(0, 9999)))

        self.assertTrue(response2.method_id)
        self.assertTrue(isinstance(response2, Object))

        response3 = self.pontopass.user(user).device.list()

        self.assertTrue(isinstance(response3, list))
        self.assertTrue(response3)

    def test_remove_devices(self):
        user = u'vinicius_{0}'.format(randint(0, 9999))
        name = u'Vinícius Cainelli'
        mobile_namber = randint(10000000000, 99999999999)

        response = self.pontopass.user.add(user=user, name=name)

        self.assertTrue(response.id)
        self.assertTrue(isinstance(response, Object))

        self.users_to_remove.append(user)

        response2 = self.pontopass.user(user).device.add(Pontopass.SMS, mobile_namber, 'desc_{0}'.format(randint(0, 9999)))

        self.assertTrue(response2.method_id)
        self.assertTrue(isinstance(response2, Object))

        response3 = self.pontopass.user(user).device.list()

        self.assertTrue(isinstance(response3, list))
        self.assertTrue(response3)
        self.assertEqual(len(response3), 1)

        for device in response3:
            response4 = self.pontopass.user(user).device.delete(device.id)
            self.assertTrue(response4)
