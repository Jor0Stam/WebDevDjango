from django.test import TestCase, Client
from django.urls import reverse_lazy, reverse

from .factories import CategoryFactory, OfferFactory, UserFactory
from .models import Offer, Category

from test_plus.test import TestCase as PlusTestCase
from faker import Factory
import tempfile

faker = Factory.create()

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
        self.user = UserFactory()
        self.category = CategoryFactory()
        self.url = reverse('offer:create_offer')

    def test_anon_can_not_access_create_form(self):
        response = self.client.get(self.url)
        self.assertEqual(302, response.status_code)
        self.assertEqual(0, Offer.objects.count())

    def test_loged_user_can_create_offer(self):
        temp_img = tempfile.NamedTemporaryFile(suffix='.jpg').name

        data = {
                'title': faker.word(),
                'description': faker.text(),
                'category': self.category.id,
                'image': temp_img
                }

        logged = self.client.force_login(self.user)
        import ipdb; ipdb.set_trace() # BREAKPOINT
        response = self.client.post(self.url, data=data)
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, Offer.objects.count())

    def tearDown(self):
        self.client.logout()
