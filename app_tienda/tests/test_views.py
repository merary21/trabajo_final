from django.test import TestCase, Client
from django.urls import reverse
from app_tienda.models import *

class test_views(TestCase):
    def test_create(self):
     client = Client()

     response = client.get(reverse('inicio'))

     self.assertEqual(response.status_code,200)
     self.assertTemplateUsed(response, 'inicio.html')