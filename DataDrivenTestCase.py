from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import XLUtils

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path = "D://certificates/Selenium/Login1.xlsx"

rows = XLUtils.getRowCount(path,'Sheet1')
#cols = XLUtils.getColumnCount(path,'Sheet1')
for r in range(2, rows+1):
    username = XLUtils.readData(path,'Sheet1',r,1)
    password = XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("submit").click()

    if driver.title == "Login: Mercury Tours":
        print("Test is passed")
        XLUtils.writeData(path, "Sheet1",r,3,"Test Passed")

    else:
        print("Test Failed")
        XLUtils.writeData(path, "Sheet1",r,3,"Test Failed")

    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()




quit
