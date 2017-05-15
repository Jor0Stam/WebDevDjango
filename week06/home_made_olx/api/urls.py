from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

from .views import OfferListCreateView, OfferDetailView

urlpatterns = [
    url(r'offer/$', OfferListCreateView.as_view(), name='create_offer'),
    url(r'offer/(?P<pk>.*)$', OfferDetailView.as_view(), name='create_offer'),
    url(r'^api-token-auth/', obtain_jwt_token),
]
