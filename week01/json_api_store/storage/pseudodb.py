import uuid
import json
from django.conf import settings
import os
from storage.exceptions import NoSuchUser


def get_uuid4():
    return str(uuid.uuid4())


def user_exists(id):
    if not os.path.exists(id):
        raise NoSuchUser


#
def fill_user_db(id, data):
    # import ipdb; ipdb.set_trace()
    id_file_name = settings.JSON_DATABASE_DIR + id + '.json'
    with open(id_file_name, 'w') as f:
        f.write(json.dumps(data, indent=4))


# gets content of users db
def get_user_db(id):
    id_file_name = settings.JSON_DATABASE_DIR + id + '.json'
    user_exists(id_file_name)
    data = {}

    with open(id_file_name, 'r') as f:
        data = json.loads(f.read())
    return data


# creates user
def create_user():
    id = get_uuid4()
    fill_user_db(id, data={})

    return id


# adds new key value pair
def add_key_value(id, key, value):
    data = get_user_db(id)
    data[key] = value
    fill_user_db(id, data=data)

    return data


def get_value(id, key):
    return get_user_db(id).get(key)


def delete_value(id, key):
    data = get_user_db(id)
    deleted_element = data.pop(key)
    fill_user_db(id, data)

    return deleted_element
