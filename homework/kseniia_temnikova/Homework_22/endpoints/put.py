import allure
import requests
from endpoints.endpoint import Endpoint

class PutObject(Endpoint):

    @allure.step('Changing an object')
    def change_object_completely(self, id, payload, headers = None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{id}',
            json = payload,
            headers = headers
        )
        print(self.response.status_code)
        self.json = self.response.json()




