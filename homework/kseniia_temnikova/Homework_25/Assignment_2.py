import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

SUBJECT_INPUT = (By.ID, "subjectsInput")
OPTION = (By.XPATH, "//div[contains(@class,'subjects-auto-complete__option')]")
CHIP_LABELS = (By.XPATH, "//div[contains(@class,'subjects-auto-complete__multi-value__label')]")


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    chrome_driver.set_window_size(375, 812)
    yield chrome_driver


def find_element_by(driver, by, arg):
    element = driver.find_element(by, arg)
    return element


def find_element_by_and_send_key(driver, by, arg, key):
    element = find_element_by(driver, by, arg)
    element.send_keys(key)
    return element


def find_element_by_and_click(driver, by, arg):
    element = find_element_by(driver, by, arg)
    element.click()


def find_element_by_and_select_by_value(driver, by, arg, value):
    element = find_element_by(driver, by, arg)
    element_dropdown = Select(element)
    element_dropdown.select_by_value(value)


def find_element_by_and_click_by_idx(driver, By, arg, idx):
    elements = driver.find_elements(By, arg)
    return elements[idx].click()


def type_subject(driver, prefix: str):
    wait = WebDriverWait(driver, 10)
    field = wait.until(EC.element_to_be_clickable(SUBJECT_INPUT))
    field.send_keys(prefix)
    wait.until(EC.visibility_of_element_located(OPTION))
    return field


def pick_option_by_text(driver, text: str):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(SUBJECT_INPUT))
    xpath = f"//div[contains(@class,'subjects-auto-complete__option') and normalize-space()='{text}']"
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


def selected_subjects(driver):
    return [el.text.strip() for el in driver.find_elements(*CHIP_LABELS)]


def test_send_data(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    driver.execute_script(
        "window.scrollTo(0, 400);")
    find_element_by_and_send_key(driver, By.ID, 'firstName', 'Linda')
    find_element_by_and_send_key(driver, By.ID, 'lastName', 'Piney')
    find_element_by_and_send_key(driver, By.ID, 'userEmail', 'testuser@mail.com')
    find_element_by_and_click(driver, By.XPATH, "//label[@for='gender-radio-2']")
    find_element_by_and_send_key(driver, By.ID, 'userNumber', '1234567890')
    driver.execute_script("window.scrollTo(0, 600);")
    find_element_by_and_click(driver, By.ID, 'dateOfBirthInput')
    find_element_by_and_select_by_value(driver, By.CLASS_NAME, 'react-datepicker__month-select', '5')
    find_element_by_and_select_by_value(driver, By.CLASS_NAME, 'react-datepicker__year-select', '1939')
    find_element_by_and_click(driver, By.CLASS_NAME, "react-datepicker__day--012")

    type_subject(driver, "ma")
    pick_option_by_text(driver, "Maths")

    driver.execute_script("window.scrollTo(0, 1100);")
    find_element_by_and_click(driver, By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys('Testing address')

    driver.find_element(By.ID, 'state').click()
    state_input = driver.find_element(By.ID, 'react-select-3-input')
    state_input.send_keys('NCR')
    state_input.send_keys(Keys.ENTER)

    driver.find_element(By.ID, 'city').click()
    city_input = driver.find_element(By.ID, 'react-select-4-input')
    city_input.send_keys('Delhi')
    city_input.send_keys(Keys.ENTER)
    find_element_by_and_click(driver, By.ID, 'submit')
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "div.modal-body table.table"
    )))

    def get_value(label_text: str) -> str:
        xpath = f".//td[normalize-space()='{label_text}']/following-sibling::td[1]"
        cell = table.find_element(By.XPATH, xpath)
        return cell.text.strip()

    full_name = get_value("Student Name")
    email = get_value("Student Email")
    gender = get_value("Gender")
    mobile = get_value("Mobile")
    birthdate = get_value("Date of Birth")
    subjects = get_value('Subjects')
    hobbies = get_value("Hobbies")
    address = get_value('Address')
    first_name, last_name = full_name.split(maxsplit=1)
    assert first_name == "Linda"
    assert last_name == "Piney"
    assert email == "testuser@mail.com"
    assert gender == "Female"
    assert mobile == "1234567890"
    assert birthdate == '12 June,1939'
    assert subjects == 'Maths'
    assert hobbies == 'Sports'
    assert address == 'Testing address'
