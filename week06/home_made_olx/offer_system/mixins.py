from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Offer

class BaseMixin(UserPassesTestMixin):

    def test_func(self):
        return True

class CanUpdateOfferMixin(BaseMixin):

    def test_func(self):
        offer_id = self.kwargs.get('pk')
        offer = Offer.objects.filter(id=int(offer_id)).first()
        if not offer.author == self.request.user:
            return False
        return True and super().test_func()



class IsSuperUserMixin(BaseMixin):

    def test_func(self):
        if not self.request.user.is_superuser:
            return False
        return True and super().test_func()
