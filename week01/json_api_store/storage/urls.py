from django.conf.urls import url
from django.contrib import admin

from .views import create_user, put_info

urlpatterns = [
        url(r'^create-user/$', create_user),
        url(r'^(?P<key>.*)/$', put_info)
]
