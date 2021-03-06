import factory
from faker import Factory

from .models import Offer, Category
from django.contrib.auth.models import User

faker = Factory.create()


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda _: faker.word())


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: faker.name())
    password = 'CheekiBreeki'


class OfferFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Offer

    title = factory.LazyAttribute(lambda _: faker.word())
    description = factory.LazyAttribute(lambda _:faker.text())
    image = factory.django.ImageField(filename=(lambda _: faker.name()))

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
