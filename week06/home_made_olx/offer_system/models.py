from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

from djmoney.models.fields import MoneyField

from .queries import OfferQuerySet

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Offer(models.Model):
    objects = models.Manager()
    stat_objects = OfferQuerySet().as_manager()

    title = models.CharField(max_length=255)
    category = models.ManyToManyField('Category', related_name='offers')
    price = MoneyField(max_digits=10,
                              decimal_places=2,
                              default_currency='BGN')
    description = models.TextField()

    image = models.ImageField()

    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               related_name='offers')

