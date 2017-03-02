from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import json
from uuid import uuid4
# Create your views here.


def create_user(request):
    if request.method != 'GET':
        return HttpResponse(status=405)
    new_identifier = str(uuid4())
    with open(new_identifier + '.json', 'w') as f:
        f.write(json.dumps(new_identifier))
    return HttpResponse(new_identifier)

def put_in_storage(key, data):
    with open(key + '.json', 'w') as f:
        f.write(json.dumps(data))


def put_info(request, key = ''):
    # import ipdb; ipdb.set_trace()
    if request.method != 'POST':
        return HttpResponse(status=405)
    put_in_storage(request.body.decode('utf-8'), data={'test': 1})
    return HttpResponse(status=200)
