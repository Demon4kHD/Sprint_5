from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import links
import locators
import data_generator


class TestRegistration:
    @pytest.mark.parametrize('length_pass', [6, 7, 25, 49, 50])
    def test_registration_valid_email_and_password(self, length_pass, start_driver):
        self.driver = start_driver
        self.user_data = data_generator.create_valid_email_and_password(length_pass)
        self.driver.get(links.REGISTRATION_URL)
        time.sleep(1)
        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_NAME).send_keys(
            self.user_data[0])
        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_EMAIL).send_keys(
            self.user_data[1])
        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_PASSWORD).send_keys(
            self.user_data[2])
        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_BUTTON_GET_REG).click()
        time.sleep(1)

        assert links.AUTHORIZATION_URL == self.driver.current_url

    @pytest.mark.parametrize('length_pass', ['None', 1, 3, 4, 5])
    def test_registration_valid_email_and_not_valid_password(self, length_pass, start_driver):
        self.driver = start_driver
        self.user_data = data_generator.create_valid_email_and_password(length_pass)
        self.driver.get(links.REGISTRATION_URL)
        time.sleep(1)
        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_NAME).send_keys(
            self.user_data[0])
        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_EMAIL).send_keys(
            self.user_data[1])
        if length_pass != 'None':
            self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_INPUT_PASSWORD).send_keys(
                self.user_data[2])

        self.driver.find_element(By.XPATH, locators.RegistrationPageElements.REG_BUTTON_GET_REG).click()
        time.sleep(1)

        assert links.AUTHORIZATION_URL != self.driver.current_url
