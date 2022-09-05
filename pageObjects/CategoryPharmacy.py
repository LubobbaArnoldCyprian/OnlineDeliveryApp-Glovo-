import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PharmacyPage:
    pharmacy_button_xpath = "//a[@href='/ug/en/kampala/pharmacy_3/']"
    pharmacy_select_xpath = "//a[@href='/ug/en/kampala/farak-pharmacy-kpa/']"
    pharmacy_menu_xpath = "//mark[normalize-space()='Menu']"
    menu_selection_xpath = "//body[starts-with(text(),'Creams')]"

    def __init__(self, driver):
        self.driver = driver

    def pharmacy(self):
        self.driver.find_element(By.XPATH, self.pharmacy_button_xpath).click()

    def setPharmacy(self):
        self.driver.find_element(By.XPATH, self.pharmacy_select_xpath).click()

    def clickMenu(self):
        self.driver.find_element(By.XPATH, self.pharmacy_menu_xpath).click()

    # def selectMenu(self):
    #     self.driver.find_element(By.XPATH, self.selectMenu).click()










