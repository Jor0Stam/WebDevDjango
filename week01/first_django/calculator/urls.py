from django.conf.urls import url
from calculator.views import add, multiply, power, call_fact


urlpatterns = [
    url(r'add/([0-9]+)/([0-9]+)/', add),
    url(r'multiply/([0-9]+)/([0-9]+)/$', multiply),
    url(r'power/([0-9]+)/([0-9]+)/$', power),
    url(r'fact/([0-9]+)/$', call_fact)
]
