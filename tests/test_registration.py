from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import links
import locators
import data_generator


class TestRegistration:
    @pytest.mark.parametrize('length_pass', [6, 7, 25, 49, 50])
    def test_registration_valid_email_and_password(self, length_pass, start_driver):
        driver = start_driver
        user_data = data_generator.create_valid_email_and_password(length_pass)
        driver.get(links.REGISTRATION_URL)

        driver.find_element(*locators.RegistrationPageElements.REG_INPUT_NAME).send_keys(
            user_data[0])
        driver.find_element(*locators.RegistrationPageElements.REG_INPUT_EMAIL).send_keys(
            user_data[1])
        driver.find_element(*locators.RegistrationPageElements.REG_INPUT_PASSWORD).send_keys(
            user_data[2])
        driver.find_element(*locators.RegistrationPageElements.REG_BUTTON_GET_REG).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            locators.AuthorizationPageElements.AUTH_H2_ENTRANCE))

        assert links.AUTHORIZATION_URL == driver.current_url

    @pytest.mark.parametrize('length_pass', [1, 2, 4, 5])
    def test_registration_valid_email_and_not_valid_password(self, length_pass, start_driver):
        driver = start_driver
        user_data = data_generator.create_valid_email_and_password(length_pass)
        driver.get(links.REGISTRATION_URL)
        driver.find_element(*locators.RegistrationPageElements.REG_INPUT_NAME).send_keys(
            user_data[0])
        driver.find_element(*locators.RegistrationPageElements.REG_INPUT_EMAIL).send_keys(
            user_data[1])
        driver.find_element(*locators.RegistrationPageElements.REG_INPUT_PASSWORD).send_keys(
            user_data[2])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            locators.RegistrationPageElements.REG_BUTTON_GET_REG)).click()

        message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            locators.RegistrationPageElements.REG_ERROR_MESSAGE))

        assert message.text == 'Некорректный пароль'
