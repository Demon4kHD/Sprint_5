from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import links
import locators

class TestUserGoToPersonalAccount:
    def test_authorize_user_click_personal_account(self, authorization_user):
        driver = authorization_user
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.MainPageElements.MAIN_BURGER_BUN_GROUP))
        driver.find_element(*locators.AllPagesElements.TOPLINE_ACCOUNT).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.PersonalAccountElements.ACC_EXIT_BUTTON))

        assert driver.current_url == links.PROFILE_URL
