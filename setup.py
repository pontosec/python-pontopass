#!/usr/bin/env python
import os
from setuptools import setup

version = '0.1.dev'

install_requires = ['requests']

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='pontopass',
    version=version,
    description='This package is a client to pontopass api',
    long_description=long_description,
    url='https://github.com/pontosec/python-pontopass/',
    author='Pontosec',
    author_email='contato@pontosec.com',
    packages=['pontopass'],
    zip_safe=False,
    install_requires=install_requires,
    test_suite='tests.get_tests',
)
