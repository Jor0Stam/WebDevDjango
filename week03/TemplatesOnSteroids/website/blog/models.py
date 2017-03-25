from django.db import models

from django.utils import timezone, timesince

from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=500)


class Author(User):
    pass


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag, related_name='posts')
    comments = models.ManyToManyField(Comment, related_name='posts')
    authors = models.ManyToManyField(Author, related_name='authors')

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)
