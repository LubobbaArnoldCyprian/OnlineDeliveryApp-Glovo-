import time

from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    address = ReadConfig.getAddress()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        time.sleep(6)
        self.lp.started()
        time.sleep(6)
        self.lp.startedLogin()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(6)
        self.lp.setAddress(self.address)





