from django.test import TestCase, Client
from django.urls import reverse_lazy, reverse

from .factories import CategoryFactory, OfferFactory, UserFactory

from test_plus.test import TestCase as PlusTestCase

# Create your tests here.


class AuthorAuthTests(PlusTestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserFactory()

    def test_user_login(self):
        data = {'username': self.user.username,
                'password':'CheekiBreeki'
                }
        response = self.client.post(reverse('author:login'), data)
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        self.client.logout()

class CreateOfferTests(PlusTestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('offer:create_offer')

    def test_anon_can_not_access_create_form(self):
        response = self.client.get(self.url)
        self.assertEqual(302, response.status_code)

    def tearDown(self):
        self.client.logout()
