from django.conf.urls import url

from django.contrib.auth import login, logout


urlpatterns = [
    url(r'login/$', login, name='index')
]
