from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import links
import locators


class TestAuthorization:
    list_of_links = [[links.STELLAR_BURGERS_URL, locators.MainPageElements.MAIN_BUTTON_GET_AUTH],
                     [links.STELLAR_BURGERS_URL, locators.AllPagesElements.TOPLINE_ACCOUNT],
                     [links.REGISTRATION_URL, locators.RegistrationPageElements.REG_LINK_GET_AUTH],
                     [links.FORGOT_PASSWORD_URL, locators.ForgotPasswordElements.FGP_LINK_GET_AUTH]]

    @pytest.mark.parametrize('where_from, what_to_click', list_of_links)
    def test_non_authorize_user_go_to_authorization_page(self, where_from, what_to_click, start_driver):
        driver = start_driver

        driver.get(where_from)
        driver.find_element(*what_to_click).click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.AuthorizationPageElements.AUTH_H2_ENTRANCE))

        assert links.AUTHORIZATION_URL == driver.current_url

    def test_authorize_user_go_to_authorization_page(self, authorization_user):
        driver = authorization_user

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            locators.MainPageElements.MAIN_BURGER_BUN_GROUP))
        driver.find_element(*locators.AllPagesElements.TOPLINE_ACCOUNT).click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.PersonalAccountElements.ACC_EXIT_BUTTON)).click()

        assert links.PROFILE_URL == driver.current_url
