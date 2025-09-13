import requests
import allure
from endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Patching an object')
    def patch_partially(self, id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{id}',
            json=payload,
            headers=headers
        )
        print(self.response.status_code)
        self.json = self.response.json()

    @allure.step('Check name of object')
    def check_name_persists(self, payload):
        assert payload['name'] == self.json['name']
