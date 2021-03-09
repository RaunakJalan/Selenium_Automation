from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest
import HtmlTestRunner

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title,"Webpage title not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title,"Webpage title not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed...")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\certificates\Selenium\Reports'))
