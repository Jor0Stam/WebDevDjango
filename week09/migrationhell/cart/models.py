from django.db import models

import uuid

from products.models import Product
from users.models import User

# Create your models here.


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, related_name='orders')
    products = models.ManyToManyField(Product)


class Invoice(models.Model):
    company_data = models.TextField()
    order = models.OneToOneField(Order)
