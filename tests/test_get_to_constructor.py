import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import links
import locators

class TestGetToConstructor:
    @pytest.mark.parametrize('list_locators',
                             [locators.AllPagesElements.TOPLINE_CONSTRUCTOR, locators.AllPagesElements.TOPLINE_LOGO])
    def test_from_page_profile_authorize_user_click_to_constuctor_and_logo(self, list_locators, authorization_user):
        driver = authorization_user

        driver.find_element(*locators.AllPagesElements.TOPLINE_ACCOUNT).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.PersonalAccountElements.ACC_EXIT_BUTTON))
        driver.find_element(*list_locators).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locators.MainPageElements.MAIN_SAUCE_GROUP))

        assert driver.current_url == links.STELLAR_BURGERS_URL
