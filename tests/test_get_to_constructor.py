import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import data
import links
import locators

class TestGetToConstructor:
    @pytest.mark.parametrize('list_locators',
                             [locators.AllPagesElements.TOPLINE_CONSTRUCTOR, locators.AllPagesElements.TOPLINE_LOGO])
    def test_authorize_user_click_to_constuctor_and_logo(self, list_locators, registration_user):
        self.driver = registration_user
        self.driver.find_element(By.XPATH, list_locators).click()
        time.sleep(1)

        assert self.driver.current_url == links.STELLAR_BURGERS_URL
