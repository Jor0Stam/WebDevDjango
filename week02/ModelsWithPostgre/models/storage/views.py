from django.shortcuts import render
from .models import User, Storage
from django.http import JsonResponse
from uuid import uuid4
from json import loads, dumps

# Create your views here.

def create_user_view(request):
    new_user = User.objects.create(name=uuid4())
    return JsonResponse({'id': str(new_user.name)})


def add_item_view(request, id):
    data = request.body.decode('utf-8')
    try:
        data = loads(data)
    except ValueError:
        return JsonResponse({'status':'error'}, status=404)

    key = data['key']
    value = data['value']

    owner = User.objects.filter(name=id)
    if not owner:
        return JsonResponse({'status':'error'}, status=404)

    Storage.objects.create(owner_id=owner[0].id, key=key, value=value)
    return JsonResponse({'Status': 'Success'}, status=201)


def manager_view(request, id, key):
    if request.method == 'GET':
        return get_value_view(request, id, key)
    if request.method == 'DELETE':
        return delete_key_view(request, id, key)
    return JsonResponse({'status': request.method}, status=404)

def get_value_view(request, id, key):
    owner = User.objects.get(name=id)
    value = owner.storage_set.filter(key=key)
    if not value:
        return JsonResponse({'status':'error'}, status=404)
    return JsonResponse({'value': value[0].value})


def delete_key_view(request, id, key):
    owner = User.objects.filter(name=id)
    if not owner:
        return JsonResponse({'error': 'No such user'}, status=404)
    owner_id = owner[0].id
    storage = Storage.objects.filter(owner=owner_id)
    if not storage:
        return JsonResponse({'status': 'KeyError'}, status=404)
    value = storage[0].value
    storage = Storage.objects.filter(owner=owner_id).delete()
    return JsonResponse({'value': value}, status=202)



