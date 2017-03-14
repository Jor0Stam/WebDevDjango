from django.db import models

from django.utils import timezone, timesince
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag, related_name = 'posts')

    def save(*args, **kwargs):
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)

class Comment(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=500)
