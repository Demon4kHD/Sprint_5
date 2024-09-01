import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import links
import data_generator
import random


@pytest.fixture
def start_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def registration_user(start_driver):
    driver = start_driver
    driver.get(links.REGISTRATION_URL)

    user_data = data_generator.create_valid_email_and_password(random.randint(6, 12))
    driver.find_element(*locators.RegistrationPageElements.REG_INPUT_NAME).send_keys(user_data[0])
    driver.find_element(*locators.RegistrationPageElements.REG_INPUT_EMAIL).send_keys(user_data[1])
    driver.find_element(*locators.RegistrationPageElements.REG_INPUT_PASSWORD).send_keys(user_data[2])
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        locators.RegistrationPageElements.REG_BUTTON_GET_REG)).click()

    return driver, user_data

@pytest.fixture
def authorization_user(registration_user):
    driver, user_data = registration_user
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        locators.AuthorizationPageElements.AUTH_H2_ENTRANCE))

    driver.find_element(*locators.AuthorizationPageElements.AUTH_INPUT_EMAIL).send_keys(user_data[1])
    driver.find_element(*locators.AuthorizationPageElements.AUTH_INPUT_PASSWORD).send_keys(user_data[2])
    driver.find_element(*locators.AuthorizationPageElements.AUTH_BUTTON_GET_AUTH).click()

    return driver
