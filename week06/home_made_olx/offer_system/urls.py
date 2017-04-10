from django.conf.urls import url

from .views import OfferListView, CreateOfferView, get_stats_view, OfferUpdate, StatisticsList


urlpatterns = [
    url(r'create-offer/$', CreateOfferView.as_view(), name='create_offer'),
    url(r'stats/$', StatisticsList.as_view(), name='stats'),
    url(r'update-offer/(?P<pk>\d+)/$', OfferUpdate.as_view(), name='update_offer'),
    url(r'^$', OfferListView.as_view(), name='index'),
]
