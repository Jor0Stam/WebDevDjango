from django.db import models

# Create your models here.

class User(models.Model):
    name = models.UUIDField(max_length=300)


class Storage(models.Model):
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    owner = models.ForeignKey(User)
