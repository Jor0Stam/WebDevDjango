from django.conf.urls import url

from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'logout/$', logout, {'next_page': 'user/login'}, name='logout')
]
