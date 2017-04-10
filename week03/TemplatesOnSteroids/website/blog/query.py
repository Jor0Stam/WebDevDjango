from django.db import models

from .models import BlogPost

class BlogPostQuerySet(models.QuerySet):

    def get_public_posts():
        return self.filter(is_private=False)

    def get_private_posts():
        return self.filter(is_private=True)
