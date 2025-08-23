import requests


def get_all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response['data']) > 0


def add_new_object():
    body = {
         "data": {
                "color": "white",
                "size": "big"
            },
         "name": "Test"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object',
                             json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    json_response = response.json()
    id = json_response['id']
    return id


def create_object_and_validate():
    id = add_new_object()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{id}')
    assert response.json(), 'Unable to fetch object by id'
    return id


def change_object():
    id = create_object_and_validate()
    body = {
        "data": {
            "color": "black",
            "size": "big"
        },
        "name": "Change object completely"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{id}', json=body, headers=headers)
    response_body = response.json()
    assert response_body, 'Unable to fetch object by id'
    assert response_body['name'] == "Change object completely", 'Object is not changed'


def patch_object():
    id = create_object_and_validate()
    body = {
        "name": "Patched object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{id}', json=body, headers=headers)
    response_body = response.json()
    assert response_body['name'] == "Patched object", 'Object is not patched'


def delete():
    id_to_delete = add_new_object()
    object_to_delete = requests.delete(f'http://objapi.course.qa-practice.com/object/{id_to_delete}')
    delete_message = object_to_delete.text
    print(delete_message)
    assert delete_message == f'Object with id {id_to_delete} successfully deleted'


get_all_objects()
add_new_object()
create_object_and_validate()
change_object()
patch_object()
delete()
