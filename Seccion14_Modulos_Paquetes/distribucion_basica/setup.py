#importamos setu
from setuptools import setup

setup(
    name='Mensajes',
    version='1.0',
    description='Un paquete para salur y despedir',
    author='Jesus Miguel',
    author_email='hola@gmail.com',
    url='https://www.hacker.dev',
    packages=['mensajes','mensajes.hola','mensajes.adios'],
    scripts=['test.py']
)