from django.db import models


class OfferQuerySet(models.QuerySet):

    def get_top_categories(self):
        return self.values('category__name').annotate(top_offer=models.Count('category__name')).order_by('-top_offer')[:3]

    def get_top_users(self):
        return self.values('author__username').annotate(top_user=models.Count('author__username')).order_by('-top_user')[:3]

    def get_pending_offer(self):
        return self.filter(status='P')

    def get_not_pending_offer(self):
        return self.exclude(status='P')
