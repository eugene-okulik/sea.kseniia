import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_pick_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    language = driver.find_element(By.CLASS_NAME, 'form-select')
    language_dropdown = Select(language)
    language_dropdown.select_by_value('1')
    submit_button = driver.find_element(By.NAME, 'submit')
    submit_button.click()
    selected_language = driver.find_element(By.ID, 'result-text')
    assert selected_language.text == 'Python'
