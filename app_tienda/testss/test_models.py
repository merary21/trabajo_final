from django.test import TestCase
from app_tienda.models import *

class TestModels(TestCase):
    def test_create(self):
     self.clienteprueba = tblCiente.object.create(
        
         nombre = "merary",
         apellido = "Araujo",
         telefono = "74082751",
         direccion = "usulutan",
         Email = "julissa21araujo@gmail.com"
         
         )