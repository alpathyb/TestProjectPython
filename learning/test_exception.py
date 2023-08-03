# new test modul to try exception in pytest
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptionScenarios:
    @pytest.mark.exception
    def test_no_such_element_exception(self,driver):
        # go to webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # search for add button and click it
        button_add_locator = driver.find_element(By.ID, "add_btn")
        button_add_locator.click()
        # you could add time sleep or using implicitly_wait in conftest.py
        # time.sleep(5)

        # add explicitly wait
        wait = WebDriverWait(driver, 10)
        row_input_2_element = wait.until(ec.presence_of_element_located((By.ID, "row2")))

        # verify row input 2 is displayed
        assert row_input_2_element.is_displayed(), "row input 2 should shows, but it's not"
