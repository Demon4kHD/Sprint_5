import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import links
import locators

class TestExitToAccount:
    def test_authorize_user_click_exit_account(self, registration_user):
        self.driver = registration_user
        self.driver.find_element(By.XPATH, locators.AllPagesElements.TOPLINE_ACCOUNT).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, locators.PersonalAccountElements.ACC_EXIT_BUTTON).click()
        time.sleep(1)

        assert self.driver.current_url == links.AUTHORIZATION_URL
