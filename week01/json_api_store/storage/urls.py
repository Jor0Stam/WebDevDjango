from django.conf.urls import url
from .views import create_user_view, add_item_view, manager_view

urlpatterns = [
    # url(r'^(?P<key>.*)/$', put_info)
    url(r'^create-user/$', create_user_view),
    url(r'^(?P<id>.*)/', add_item_view),
    url(r'(?P<id>.*)/(?P<key>.*)/',manager_view )
]
