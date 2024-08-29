import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import locators
import links
import data_generator
import time
import random


@pytest.fixture
def start_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def registration_user():
    driver = webdriver.Chrome()
    driver.get(links.REGISTRATION_URL)
    user_data = data_generator.create_valid_email_and_password(random.randint(6, 12))
    time.sleep(1)
    driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_NAME).send_keys(user_data[0])
    driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_EMAIL).send_keys(user_data[1])
    driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_PASSWORD).send_keys(
        user_data[2])
    driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_BUTTON_GET_REG).click()
    time.sleep(1)
    driver.find_element(By.XPATH, locators.AuthorizationPageElements.AUTH_INPUT_EMAIL).send_keys(user_data[1])
    driver.find_element(By.XPATH, locators.AuthorizationPageElements.AUTH_INPUT_PASSWORD).send_keys(user_data[2])
    driver.find_element(By.XPATH, locators.AuthorizationPageElements.AUTH_BUTTON_GET_AUTH).click()
    time.sleep(1)
    yield driver
    driver.quit()
