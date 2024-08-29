import pytest
from selenium.webdriver.common.by import By
import time
import links
import locators


class TestSelectGroupOfBurger:
    data_list = [locators.MainPageElements.MAIN_BURGER_BUN_GROUP,
                  locators.MainPageElements.MAIN_SAUCE_GROUP,
                  locators.MainPageElements.MAIN_FILLING_GROUP]

    @pytest.mark.parametrize('selected_group', data_list)
    def test_selecting_group_burger_is_current_other_is_no_select_by_tap(
            self, selected_group, start_driver):
        search_string = 'tab_tab_type_current__'

        self.driver = start_driver
        self.driver.get(links.STELLAR_BURGERS_URL)
        time.sleep(1)
        if selected_group is not locators.MainPageElements.MAIN_BURGER_BUN_GROUP:
            self.driver.find_element(By.XPATH, selected_group).click()
        time.sleep(1)
        comparing_value_of_group_burger_bun = (
            self.driver.find_element(By.XPATH, locators.MainPageElements.MAIN_PARENT_ELEMENT_BURGER_BUN).
            get_attribute('class'))
        comparing_value_of_group_souce = (
            self.driver.find_element(By.XPATH, locators.MainPageElements.MAIN_PARENT_ELEMENT_SAUCE).
            get_attribute('class'))
        comparing_value_of_group_filling = (
            self.driver.find_element(By.XPATH, locators.MainPageElements.MAIN_PARENT_ELEMENT_FILLING).
            get_attribute('class'))
        time.sleep(1)
        if selected_group == self.data_list[0]:
            assert search_string in comparing_value_of_group_burger_bun
            assert search_string not in comparing_value_of_group_souce
            assert search_string not in comparing_value_of_group_filling
        elif selected_group == self.data_list[1]:
            assert search_string not in comparing_value_of_group_burger_bun
            assert search_string in comparing_value_of_group_souce
            assert search_string not in comparing_value_of_group_filling
        else:
            assert search_string not in comparing_value_of_group_burger_bun
            assert search_string not in comparing_value_of_group_souce
            assert search_string in comparing_value_of_group_filling

    data_list_elements = [locators.MainPageElements.MAIN_FIRST_SCROLL_ELEMENT,
                          locators.MainPageElements.MAIN_SECOND_SCROLL_ELEMENT,
                          locators.MainPageElements.MAIN_THIRD_SCROLL_ELEMENT]
