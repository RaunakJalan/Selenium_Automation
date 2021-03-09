from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

driver.save_screenshot("D:\certificates\Selenium\homePage2.jpg")
driver.get_screenshot_as_file("D:\certificates\Selenium\homePage.png") #Takes only png else generate warning


time.sleep(3)
driver.quit()
