import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import data
import links
import locators

class TestUserGoToPersonalAccount:
    def test_autorize_user_click_personal_account(self, registration_user):
        self.driver = registration_user
        self.driver.find_element(By.XPATH, locators.AllPagesElements.TOPLINE_ACCOUNT).click()
        time.sleep(1)
        assert self.driver.current_url == links.PROFILE_URL