from django.conf.urls import url
from .views import create_user_view, add_item_view, manager_view

uuid_pattern = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'

urlpatterns = [
    url(r'^create-user/$', create_user_view),
    url(r'(?P<id>{})/(?P<key>.*)/'.format(uuid_pattern), manager_view),
    url(r'^(?P<id>{})/'.format(uuid_pattern), add_item_view),
]
