import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()
    time.sleep(5)
    hello_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
    )
    print(hello_text.text)
