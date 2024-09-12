from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import links
import locators

class TestExitToAccount:
    def test_authorize_user_click_exit_account(self, authorization_user):
        driver = authorization_user
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.MainPageElements.MAIN_BURGER_BUN_GROUP))
        driver.find_element(*locators.AllPagesElements.TOPLINE_ACCOUNT).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(locators.PersonalAccountElements.ACC_EXIT_BUTTON)).click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            locators.AuthorizationPageElements.AUTH_H2_ENTRANCE))

        assert driver.current_url == links.AUTHORIZATION_URL
