from django.conf.urls import url

from .views import OfferListView, CreateOfferView, get_stats_view, OfferUpdate, StatisticsList, UpdatePendingOffer, PendingOffers, OfferDelete
from .views import ApprovedRejectedOffers, MyOffersView

urlpatterns = [
    url(r'create-offer/$',CreateOfferView.as_view(), name='create_offer'),
    url(r'my-offers/$',MyOffersView.as_view(), name='my_offer'),
    url(r'stats/$', StatisticsList.as_view(), name='stats'),
    url(r'update-offer/(?P<pk>\d+)/$',OfferUpdate.as_view(), name='update_offer'),
    url(r'delete-offer/(?P<pk>\d+)/$',OfferDelete.as_view(), name='delete_offer'),
    url(r'pending-offers/$', PendingOffers.as_view(), name='pending_offers'),
    url(r'approved-rejected-offers/$', ApprovedRejectedOffers.as_view(), name='approved_rejected_offers'),
    url(r'pending-offer/(?P<pk>\d+)/$', UpdatePendingOffer.as_view(), name='change_status'),
    url(r'^$', OfferListView.as_view(), name='index'),
]
