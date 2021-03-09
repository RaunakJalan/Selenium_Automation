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

        #assertEqual
        #self.assertEqual("Google",titleOfWebPage,"Title does not match")
        #assertNotEqual
        self.assertNotEqual("Googled", titleOfWebPage,"Titles match")

if __name__ == "__main__":
    unittest.main()
