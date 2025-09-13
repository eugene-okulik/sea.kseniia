import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    @allure.step('Creating new object')
    def add_new_object(self, payload, headers):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
