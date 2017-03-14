from django.conf.urls import url, include

from .views import create_user_view, add_key, manager_view, user_detail

uuid_pattern = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'

storage_patterns = [
    url(r'^create-user/$', create_user_view),
    url(r'(?P<identifier>{})/(?P<key>.*)/'.format(uuid_pattern), manager_view),
    url(r'^(?P<identifier>{})/$'.format(uuid_pattern), add_key),
]

urlpatterns = [
    url(r'^storage/', include(storage_patterns)),
    url(r'user-detail/(?P<identifier>{})/$'.format(uuid_pattern), user_detail, name='user_detail'),
    url(r'(?P<identifier>{})/$'.format(uuid_pattern), add_key, name='add_key'),
    url(r'(?P<identifier>{})/(?P<key>.*)/$'.format(uuid_pattern), user_detail, name='user_detail_key'),
]
