import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(options = options,executable_path="D:/certificates/Selenium/Drivers/chromedriver.exe")

        self.driver.get("https://www.google.com/")
        print("Title of the page is :"+self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(options = options,executable_path="D:/certificates/Selenium/Drivers/chromedriver.exe")

        self.driver.get("https://www.bing.com/")
        print("Title of the page is :"+self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
