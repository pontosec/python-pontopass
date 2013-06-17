# coding: utf-8
import os
import unittest
from pontopass import Pontopass


PONTOPASS_API_USER = os.getenv('PONTOPASS_API_USER')
PONTOPASS_API_PASSWORD = os.getenv('PONTOPASS_API_PASSWORD')


class ClientTestCase(unittest.TestCase):

    def test_adduser(self):
        pontopass = Pontopass(
            api_user=PONTOPASS_API_USER,
            api_pass=PONTOPASS_API_PASSWORD,
        )
        pontopass.user.add(user='antonio')
