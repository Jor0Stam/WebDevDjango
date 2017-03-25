from django.shortcuts import render
from .models import User, Storage
from django.http import JsonResponse
from uuid import uuid4
from json import loads, dumps
from datetime import datetime
from django.urls import reverse

# Create your views here.

def index(request):
    user_num = len(list(User.objects.all()))
    keys_num = len(list(Storage.objects.all()))
    histogram = 'SOON'
    users = list(User.objects.all())
    return render(request, 'index.html', locals())


def create_user_view(request):
        new_user = User.objects.create(identifier=uuid4(), created_at=datetime.now())
        return JsonResponse({'identifier': str(new_user.identifier)})

def user_detail(request, identifier, key=None):
    owner = User.objects.filter(identifier=identifier).first()
    kvs = Storage.objects.filter(user_id=owner)
    if key:
        key = key
        value = ''
        for storage in kvs:
            if storage.key == key:
                value = storage.value
        return render(request, 'user_detail_key.html', locals())
    return render(request, 'user_detail.html', locals())


def add_key(request, identifier):
    owner = User.objects.filter(identifier=identifier)

    if not owner:
        error = 'No Such User!'
        return render(request, 'add_key.html', locals(), status=404)

    if request.method == 'POST':
        owner = owner.first()
        key = request.POST.get('key', '')
        value = request.POST.get('value', '')

        storage = Storage.objects.filter(user=owner, key=key)
        if storage:
            storage.value = value
            storage.save()
        else:
            Storage.objects.creatfe(user=owner, key=key, value=value)

        # Finish That !
        # return redirect(reverse('user-detail', kwargs={'identifier': identifier}))

        return render(request, 'add_key.html', locals(), status=201)


    return render(request, 'add_key.html', locals())


def manager_view(request, identifier, key):
    if request.method == 'GET':
        return get_value_view(request, identifier, key)
    if request.method == 'DELETE':
        return delete_key_view(request, identifier, key)
    return JsonResponse({'status': request.method}, status=403)

def get_value_view(request, identifier, key):
    owner = User.objects.get(identifier=identifier)
    value = owner.data.filter(key=key)

    if not value:
        return JsonResponse({'status':'error'}, status=404)

    return JsonResponse({'value': value[0].value})


def delete_key_view(request, identifier, key):
    owner = User.objects.filter(identifier=identifier).first()
    if not owner:
        return JsonResponse({'error': 'No such user'}, status=404)
    # owner_identifier = owner[0].identifier
    storage = Storage.objects.filter(owner=owner, key=key)

    if not storage:
        return JsonResponse({'status': 'KeyError'}, status=404)
    value = storage[0].value
    storage = Storage.objects.filter(owner=owner_identifier).delete()

    return JsonResponse({'value': value}, status=202)



