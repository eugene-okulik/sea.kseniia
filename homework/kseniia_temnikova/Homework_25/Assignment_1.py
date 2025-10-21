from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_id_name(driver):
    input_data = 'cats'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.NAME, 'text_string')
    search_input.send_keys(input_data)
    search_input.submit()
    result_id = driver.find_element(By.ID, 'result-text')
    assert result_id.text == input_data
    print(result_id.text)
