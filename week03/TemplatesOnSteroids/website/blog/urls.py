from django.conf.urls import url
from .views import index, detail_blog, create_blog


urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^detail-blog/(?P<name>[\w\d\']+)$', detail_blog, name='detail-blog'),
        url(r'^create-blog/$', create_blog, name='create-blog'),
    ]
