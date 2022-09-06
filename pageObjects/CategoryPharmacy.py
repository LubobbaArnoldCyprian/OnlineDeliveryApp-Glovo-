import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PharmacyPage:
    pharmacy_button_xpath = "//a[@href='/ug/en/kampala/pharmacy_3/']"
    pharmacy_select_xpath = "//a[@href='/ug/en/kampala/farak-pharmacy-kpa/']"
    pharmacy_menu_xpath = "//mark[normalize-space()='Menu']"
    menu_selection_xpath = "//a[.='Condoms']"
    #menu_selection_xpath = "//div[@class='store__page__catalogue']"

    def __init__(self, driver):
        self.driver = driver

    def pharmacy(self):
        self.driver.find_element(By.XPATH, self.pharmacy_button_xpath).click()

    def setPharmacy(self):
        self.driver.find_element(By.XPATH, self.pharmacy_select_xpath).click()

    def clickMenu(self):
        self.driver.find_element(By.XPATH, self.pharmacy_menu_xpath).click()

    def selectMenu(self):
        scroll_condoms = self.driver.find_element(By.XPATH, self.menu_selection_xpath)
        self.driver.execute_script("arguments[0].click();", scroll_condoms)



























