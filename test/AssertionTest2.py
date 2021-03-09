#assertTrue and assertFalse
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title

        #assertTrue
        #self.assertTrue(titleOfWebPage=="Google","Title does not match")
        #assertFalse
        self.assertFalse(titleOfWebPage == "Google","Titles match")

if __name__ == "__main__":
    unittest.main()
