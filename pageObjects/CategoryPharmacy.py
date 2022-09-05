import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PharmacyPage:
    pharmacy_button_xpath = "//body/div[contains(.,'Pharmacy')]"

    def __init__(self, driver):
        self.driver = driver

    def pharmacy(self):
        self.driver.find_element(By.XPATH, self.pharmacy_button_xpath).click()





