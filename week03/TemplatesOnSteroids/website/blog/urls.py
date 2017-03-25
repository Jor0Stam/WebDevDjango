from django.conf.urls import url
from .views import index, detail_blog, create_blog, create_tag


urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^detail-blog/(?P<title>[\<\w\d\'\s]+)$', detail_blog, name='detail-blog'),
        url(r'^create-blog/$', create_blog, name='create-blog'),
        url(r'^create-tag/$', create_tag, name='create-tag'),
    ]
