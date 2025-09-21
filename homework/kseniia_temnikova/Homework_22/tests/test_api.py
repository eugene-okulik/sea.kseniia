import pytest

TEST_DATA = [
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
    }]

TEST_DATA_TO_CHANGE_COMPLETELY = [
    {
        "data": {
            "color": "white",
            "size": "big"
        },
        "name": "Test_to change"
    },
    {
        "data": {
            "color": "yellow",
            "size": "big"
        },
        "name": "Test_to_change"
    },
    {
        "data": {
            "color": "Red",
            "size": "big"
        },
        "name": "Test_to_change"
    }]

DATA_TO_PATCH = [
    {
        "name": "Patched_object"
    },
    {
        "name": "Patched_object_2"
    },
    {
        "name": "Patched_object_3"
    }]


@pytest.mark.parametrize('body', TEST_DATA)
def test_create_new_object(create_post_endpoint, body):
    create_post_endpoint.add_new_object(body, None)
    create_post_endpoint.check_status_is_200()
    create_post_endpoint.check_color_persists(body)


def test_get_by_id(created_mock_object, get_endpoint):
    id = created_mock_object['id']
    get_endpoint.get_by_id(id)
    get_endpoint.check_status_is_200()
    get_endpoint.check_color_persists(created_mock_object)


@pytest.mark.parametrize('body', TEST_DATA_TO_CHANGE_COMPLETELY)
def test_change_object_completely(created_mock_object, change_endpoint, body):
    id = created_mock_object['id']
    change_endpoint.change_object_completely(id, body)
    change_endpoint.check_status_is_200()

def test_delete_an_object(created_mock_object, delete_endpoint):
    id = created_mock_object['id']
    delete_endpoint.delete_an_object(id, None)
    delete_endpoint.check_status_is_200()


@pytest.mark.parametrize('patcher', DATA_TO_PATCH)
def test_patch_an_object(created_mock_object,  patch_endpoint, patcher):
    id = created_mock_object['id']
    patch_endpoint.patch_partially(id, patcher, None)
    patch_endpoint.check_status_is_200()
    patch_endpoint.check_name_persists(patcher)
