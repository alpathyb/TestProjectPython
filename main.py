import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Scenarios
def test_positive_login(self):
        # Open browser
        driver = webdriver.Chrome()
        time.sleep(3)

        # Go to Webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into username field
        username_locator = driver.find_element(By.XPATH, "//input[@id='username']")
        username_locator.send_keys("student")

        # Type password Password123 into password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys("Password123")

        # push submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # verify new page URL contains
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page URL contains Logged In Successfully
        text_locator = driver.find_element(By.XPATH, "//article//h1[@class='post-title']")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify new page URL contains Log Out Button
        log_out_button_locator = driver.find_element(By.XPATH, "//a[@href='https://practicetestautomation.com/practice-test-login/']")
        assert log_out_button_locator.is_displayed()
