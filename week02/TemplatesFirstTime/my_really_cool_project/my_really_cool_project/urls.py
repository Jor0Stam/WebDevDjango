from django.conf.urls import url, include
from django.contrib import admin
from api import urls as api_urls
from api.views import index, add_key, user_detail

uuid_pattern = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls), name='api_storage'),
    url(r'add-key/(?P<identifier>{})/$'.format(uuid_pattern), add_key),
    url(r'user-detail/(?P<identifier>{})/$'.format(uuid_pattern), user_detail),
    url(r'^$', index, name='index'),
    ]

