import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PharmacyPage:
    pharmacy_button_xpath = "//a[@href='/ug/en/kampala/pharmacy_3/']"
    pharmacy_select_xpath = "//a[@href='/ug/en/kampala/farak-pharmacy-kpa/']"
    pharmacy_menu_xpath = "//mark[normalize-space()='Menu']"
    menu_selection_xpath = "//a[.='Condoms']"
    item_selected_xpath = "//body[contains(.,'Durex')]"
    add_product_xpath = "//button[@data-test-id='add-button']"
    checkout_xpath = "//button[@data-test-id='checkout-button']"
    #textbox_location_xpath = "//ul[@id='el-autocomplete-3229']"
    comfirm_address_xpath = "//button[@data-test-id='location-form-submit-button']"

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

    def selectItem(self):
        self.driver.find_element(By.XPATH, self.item_selected_xpath).click()

    def addItem(self):
        self.driver.find_element(By.XPATH, self.add_product_xpath).click()

    def checkOut(self):
        self.driver.find_element(By.XPATH, self.checkout_xpath).click()

    # def locationFloor(self, floor):
    #     textbox_location= self.driver.find_element(By.XPATH, self.textbox_location_xpath)
    #     textbox_location.clear()
    #     textbox_location.send_keys(floor)

    def confirmAddress(self):
        self.driver.find_element(By.XPATH, self.comfirm_address_xpath).click()










































