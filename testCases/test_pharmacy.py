import time

from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.CategoryPharmacy import PharmacyPage


class Test_001_Pharmacy:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    address = ReadConfig.getAddress()

    def test_pharmacy(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.started()
        time.sleep(3)
        self.lp.startedLogin()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.setAddress(self.address)
        time.sleep(5)
        self.pp = PharmacyPage(self.driver)
        time.sleep(3)
        self.pp.pharmacy()









