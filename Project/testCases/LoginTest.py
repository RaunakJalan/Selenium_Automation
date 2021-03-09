import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sys
sys.path.append("D:\certificates\Selenium\Project")

from pageObjects.LoginPage import LoginPage
import time

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    options = Options()
    options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
    driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
    driver = webdriver.Chrome(options = options, executable_path = driver_path)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title,"Webpage title not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:\certificates\Selenium\Project\\reports"))
