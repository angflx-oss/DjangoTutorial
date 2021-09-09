from django.urls import reverse #Cambio de django.core.urlresolvers
from django.urls import resolve
from django.test import TestCase
from .views import signup

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def t1JRpfow927XUoPtmgataMC5m5aLewzNYUP(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)