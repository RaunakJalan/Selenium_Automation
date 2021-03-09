'''
Operations:
1. Capture all cookies from Browser
2. Count number of cookies
3. Read cookie pairs
4. Adding new cookies
5. Deleting specific cookie by using name of cookie
6. Deleting all cookies
'''
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

driver.get("https://www.amazon.in/")
driver.maximize_window()

#1.
cookies = driver.get_cookies()
#2.
print(len(cookies))
#Print all cookies
print(cookies)


#4.
cookie = {'name':'MyCookie', 'value':'1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))     #length after addition
print(cookies)


#5
driver.delete_cookie('MyCookie')

cookies = driver.get_cookies()
print(len(cookies))     #length after deletion
print(cookies)


#6
driver.delete_all_cookies()

cookies = driver.get_cookies()
print(len(cookies))     #length after deletion
print(cookies)


time.sleep(3)
driver.quit()
