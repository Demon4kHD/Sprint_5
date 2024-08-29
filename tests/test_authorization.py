from selenium.webdriver.common.by import By
import time
import pytest
import links
import locators
import data_generator
import random


class TestAuthorization:
    list_of_links = [[links.STELLAR_BURGERS_URL, locators.MainPageElements.MAIN_BUTTON_GET_AUTH],
                     [links.STELLAR_BURGERS_URL, locators.AllPagesElements.TOPLINE_ACCOUNT],
                     [links.REGISTRATION_URL, locators.RegistrationPageElements.REG_LINK_GET_AUTH],
                     [links.FORGOT_PASSWORD_URL, locators.ForgotPasswordElements.FGP_LINK_GET_AUTH]]

    @pytest.mark.parametrize('where_from, what_to_click', list_of_links)
    def test_non_authorize_user_go_to_authorization_page(self, where_from, what_to_click, start_driver):
        self.driver = start_driver
        self.driver.get(where_from)
        time.sleep(1)
        self.driver.find_element(By.XPATH, what_to_click).click()
        time.sleep(1)

        assert links.AUTHORIZATION_URL == self.driver.current_url

    def test_authorize_user_go_to_authorization_page(self, registration_user):
        self.driver = registration_user
        self.driver.find_element(By.XPATH, locators.AllPagesElements.TOPLINE_ACCOUNT).click()
        time.sleep(1)

        assert links.PROFILE_URL == self.driver.current_url
