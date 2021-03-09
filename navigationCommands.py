from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://www.demo.guru99.com/test/newtours/")
print(driver.title)

driver.get("http://www.pavantestingtools.com/")
time.sleep(5)
print(driver.title)

driver.back()   #Goes back one page
time.sleep(5)
print(driver.title)

driver.forward()    #Goes forward one page
time.sleep(5)
print(driver.title)

driver.quit()
