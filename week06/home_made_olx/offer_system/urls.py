from django.conf.urls import url

from .views import index_view, create_offer_view, get_stats_view


urlpatterns = [
    url(r'create-offer/$', create_offer_view, name='create_offer'),
    url(r'stats/$', get_stats_view, name='stats'),
    url(r'$', index_view, name='index'),
]
