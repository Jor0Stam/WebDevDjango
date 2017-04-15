from django.conf.urls import url

from django.contrib.auth.views import login, logout

from .views import register_view


urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'register/$', register_view, name='register'),
    url(r'logout/$', logout, {'next_page': 'user/login'}, name='logout')
]
