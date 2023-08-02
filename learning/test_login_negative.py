import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenario:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into username field
        username_locator = driver.find_element(By.XPATH, "//input[@id='username']")
        username_locator.send_keys(username)

        # Type password Password123 into password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys(password)

        # Click Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message in displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is your username is invalid
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"
