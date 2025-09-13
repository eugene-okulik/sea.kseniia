import allure
import requests
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Getting object by id')
    def get_by_id(self, id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/{id}',
            headers=headers
        )
        self.json = self.response.json()
