from django.http import JsonResponse, HttpResponse
from django.conf import settings
from json import loads
from exceptions import NoSuchUser
from .pseudodb import create_user, add_key_value, get_value, delete_value
# Create your views here.


def create_user_view(request):
    data = {'id': create_user()}
    return JsonResponse(data)


def add_item_view(request, id):
    body = request.body.decode('utf-8')
    try:
        data = loads(body)
    except ValueError:
        return JsonResponse(data={}, status=200)

    key = data['key']
    value = data['value']

    try:
        add_key_value(id=id, key=key, value=value)
    except NoSuchUser:
        data = {
            'error': 'user not found'
        }
        return JsonResponse(data=data, status=404)

    return JsonResponse(data=data, status=201)

def manager_view(request, id, key):
    if request.method == 'GET':
        return get_value_view(request, id, key)
    if request.method == 'DELETE':
        return delete_value_view(request, id, key)
    return HttpResponse(status=405)


def get_value_view(request, id, key):
    try:
        data = get_value(id, key)
    except NoSuchUser:
        data = {
            'error': 'No Such User'
        }
        return JsonResponse(data=data, status=404)
    except ValueError:
        return HttpResponse(status=404)

    if not data:
        return JsonResponse(data={'error':'No such key'}, status=404)

    return JsonResponse({'value': data})

def delete_value_view(request, id, key):
    try:
        old_key = delete_value(id, key)
    except KeyError:
        return HttpResponse(status=403)

    return HttpResponse(status=200)
