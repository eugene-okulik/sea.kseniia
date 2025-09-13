import pytest
from endpoints.create_post import CreateObject
from endpoints.get import GetObject
from endpoints.put import PutObject
from endpoints.delete import DeleteObject
from endpoints.patch import PatchObject


@pytest.fixture()
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def get_endpoint():
    return GetObject()


@pytest.fixture()
def change_endpoint():
    return PutObject()


@pytest.fixture()
def delete_endpoint():
    return DeleteObject()


@pytest.fixture()
def patch_endpoint():
    return PatchObject()


@pytest.fixture()
def created_mock_object(create_post_endpoint):
    payload = {
        "data": {
            "color": "pink",
            "size": "small"
        },
        "name": "Id_test"
    }
    create_post_endpoint.add_new_object(payload, None)
    return create_post_endpoint.json
