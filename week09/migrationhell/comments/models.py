from django.db import models

from users.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    product = models.ForeignKey('products.Product')
    text = models.TextField()

