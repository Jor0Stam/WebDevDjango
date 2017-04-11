from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import OfferListView, CreateOfferView, get_stats_view, OfferUpdate, StatisticsList


urlpatterns = [
    url(r'create-offer/$',login_required(CreateOfferView.as_view()), name='create_offer'),
    url(r'stats/$', login_required(StatisticsList.as_view()), name='stats'),
    url(r'update-offer/(?P<pk>\d+)/$',login_required(OfferUpdate.as_view()), name='update_offer'),
    url(r'^$', OfferListView.as_view(), name='index'),
]
