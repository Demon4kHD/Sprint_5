from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import links
import locators


class TestSelectGroupOfBurger:
    search_string = 'tab_tab_type_current__'

    def test_default_selecting_group_burger_is_current(self, start_driver):
        driver = start_driver
        driver.get(links.STELLAR_BURGERS_URL)

        comparing_value_of_group_burger_bun = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.MainPageElements.MAIN_PARENT_ELEMENT_BURGER_BUN)).get_attribute('class')
        comparing_value_of_group_souce = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_SAUCE).get_attribute('class')
        comparing_value_of_group_filling = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_FILLING).get_attribute('class')

        assert self.search_string in comparing_value_of_group_burger_bun
        assert self.search_string not in comparing_value_of_group_souce
        assert self.search_string not in comparing_value_of_group_filling

    def test_selecting_sauce_is_current(self, start_driver):
        driver = start_driver
        driver.get(links.STELLAR_BURGERS_URL)

        driver.find_element(*locators.MainPageElements.MAIN_SAUCE_GROUP).click()

        comparing_value_of_group_burger_bun = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.MainPageElements.MAIN_PARENT_ELEMENT_BURGER_BUN)).get_attribute('class')
        comparing_value_of_group_souce = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_SAUCE).get_attribute('class')
        comparing_value_of_group_filling = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_FILLING).get_attribute('class')

        assert self.search_string not in comparing_value_of_group_burger_bun
        assert self.search_string in comparing_value_of_group_souce
        assert self.search_string not in comparing_value_of_group_filling

    def test_selecting_filling_is_current(self, start_driver):
        driver = start_driver
        driver.get(links.STELLAR_BURGERS_URL)

        driver.find_element(*locators.MainPageElements.MAIN_FILLING_GROUP).click()

        comparing_value_of_group_burger_bun = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.MainPageElements.MAIN_PARENT_ELEMENT_BURGER_BUN)).get_attribute('class')
        comparing_value_of_group_souce = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_SAUCE).get_attribute('class')
        comparing_value_of_group_filling = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_FILLING).get_attribute('class')

        assert self.search_string not in comparing_value_of_group_burger_bun
        assert self.search_string not in comparing_value_of_group_souce
        assert self.search_string in comparing_value_of_group_filling

    def test_selecting_group_burger_is_current(self, start_driver):
        driver = start_driver
        driver.get(links.STELLAR_BURGERS_URL)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            locators.MainPageElements.MAIN_SAUCE_GROUP)).click()
        driver.find_element(*locators.MainPageElements.MAIN_BURGER_BUN_GROUP).click()

        comparing_value_of_group_burger_bun = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            locators.MainPageElements.MAIN_PARENT_ELEMENT_BURGER_BUN)).get_attribute('class')
        comparing_value_of_group_souce = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_SAUCE).get_attribute('class')
        comparing_value_of_group_filling = driver.find_element(
            *locators.MainPageElements.MAIN_PARENT_ELEMENT_FILLING).get_attribute('class')

        assert self.search_string in comparing_value_of_group_burger_bun
        assert self.search_string not in comparing_value_of_group_souce
        assert self.search_string not in comparing_value_of_group_filling
