# Importing Files
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPositiveScenarios:
    def test_positive_login(self):
        # open the browser
        driver = webdriver.Chrome()
        time.sleep(3)

        # Go to Webpage
        driver.get("https://kerja.kitalulus.com/id")
        time.sleep(2)

        # Go to Page Account
        account_button_locator = driver.find_element(By.XPATH, "//a[@href='/id/account']/button")
        account_button_locator.click()
        time.sleep(2)

        # Verify you are in Account Page
        account_url = driver.current_url
        assert account_url == "https://kerja.kitalulus.com/id/account"

        # Go to Log In by google page
        log_in_button_locator = driver.find_element(By.XPATH, "//button[@type='button']/h3[.='Log In dengan Google']")
        log_in_button_locator.click()
        time.sleep(2)





