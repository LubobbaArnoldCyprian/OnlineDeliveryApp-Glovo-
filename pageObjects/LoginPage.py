import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    getStarted_button_id = "user-register"
    getStarted_login_xpath = "//span[normalize-space()='Log in']"
    textbox_email_xpath = "//input[@name='email']"
    textbox_password_xpath = "//input[@name='password']"
    loginButton_xpath = "//span[normalize-space()='Log in with email']"
    textbox_address_xpath = "//input[@role='textbox']"

    def __init__(self, driver):
        self.driver = driver

    def started(self):
        self.driver.find_element(By.ID, self.getStarted_button_id).click()

    def startedLogin(self):
        self.driver.find_element(By.XPATH, self.getStarted_login_xpath).click()

    def setEmail(self, email):
        login_email_field = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        login_email_field.clear()
        login_email_field.send_keys(email)

    def setPassword(self, password):
        login_password_field = self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        login_password_field.clear()
        login_password_field.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.loginButton_xpath).click()

    def setAddress(self, address):
        address_field = self.driver.find_element(By.XPATH, self.textbox_address_xpath)
        address_field.clear()
        address_field.send_keys(address)
        time.sleep(5)

        #selection of the address from the drop down suggestions
        address_field.send_keys(Keys.ARROW_DOWN)
        time.sleep(5)
        address_field.send_keys(Keys.ARROW_DOWN)
        address_field.send_keys(Keys.ENTER)





