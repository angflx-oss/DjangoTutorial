from django.urls import reverse #Cambio de django.core.urlresolvers
from django.test import TestCase
from django.urls import resolve
from .views import home

#Prueba devuelve el statuscode.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

#Match urls solicitadas con urls.py
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)