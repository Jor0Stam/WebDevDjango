from django.db import models

from uuid import uuid4
from django.utils import timezone

# Create your models here.

class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class User(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(default=timezone.now)

class Storage(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    user = models.ForeignKey(User, related_name='data')
    created_at = models.DateTimeField(default=timezone.now)
