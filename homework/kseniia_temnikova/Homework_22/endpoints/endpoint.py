import allure


class Endpoint():
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check response status is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Check 'color' persists")
    def check_color_persists(self, payload):
        assert payload['data']['color'] == self.json['data']['color']
