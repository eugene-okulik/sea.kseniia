import requests
import pytest
import allure


@pytest.fixture(autouse=True)
def every_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture(scope='session', autouse=True)
def every_session():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture
def object_to_delete():
    body = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": "Test"
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Making a request'):
        response = requests.post('http://objapi.course.qa-practice.com/object',
                                 json=body, headers=headers)
        response_id = response.json()['id']
        yield response.json()
    with allure.step('Status check'):
        if response.status_code != 400:
            requests.delete(f'http://objapi.course.qa-practice.com/object/{response_id}')


@allure.feature('Object manupilaions')
@allure.story('Add new object')
@pytest.mark.parametrize('body', [
    {
        "data": {
            "color": "orange",
            "size": "big"
        },
        "name": "Test_orange"
    },
    {
        "data": {
            "color": "green",
            "size": "big"
        },
        "name": "Test_green"
    },
    {
        "data": {
            "color": "blue",
            "size": "big"
        },
        "name": "Test_blue"
    }
])
def test_add_new_object(body):
    headers = {'Content-Type': 'application/json'}
    with allure.step('Making a request'):
        response = requests.post('http://objapi.course.qa-practice.com/object',
                                 json=body, headers=headers)
    with allure.step('Status check'):
        assert response.status_code == 200, 'Status code is incorrect'
        json_response = response.json()
        assert json_response['data']['color'] == body['data']['color']


@allure.feature('Object manupilaions')
def test_get_object_by_id(object_to_delete):
    id = object_to_delete['id']
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{id}')
    assert response.json(), 'Unable to fetch object by id'


@allure.feature('Object manupilaions')
@allure.story('Change existing object')
@pytest.mark.critical
def test_change_object(object_to_delete):
    body = {
        "data": {
            "color": "black",
            "size": "big"
        },
        "name": "Change object completely"
    }
    headers = {'Content-Type': 'application/json'}
    id = object_to_delete['id']
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{id}', json=body, headers=headers)
    response_body = response.json()
    assert response_body, 'Unable to fetch object by id'
    with allure.step('Object is changed'):
        assert response_body['name'] == "Change object completely", 'Object is not changed'


@allure.feature('Object manupilaions')
@allure.story('Patch existing object')
def test_patch_object(object_to_delete):
    id = object_to_delete['id']
    body = {
        "name": "Patched object"
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Making a request'):
        response = requests.patch(f'http://objapi.course.qa-practice.com/object/{id}', json=body, headers=headers)
        response_body = response.json()
    with allure.step('Patch name check'):
        assert response_body['name'] == "Patched object", 'Object is not patched'


@allure.feature('Object manupilaions')
@allure.story('Delete existing object')
@pytest.mark.medium
def test_delete(object_to_delete):
    id_to_delete = object_to_delete['id']
    with allure.step('Making a request'):
        object_to_delete = requests.delete(f'http://objapi.course.qa-practice.com/object/{id_to_delete}')
        delete_message = object_to_delete.text
    with allure.step('Removal is completed'):
        assert delete_message == f'Object with id {id_to_delete} successfully deleted'
