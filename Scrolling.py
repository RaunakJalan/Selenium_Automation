from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

'''
1. By pixel:
    driver.execute_script("window.scrollBy(0,500)","")
2. Scroll till element found:
    Element = driver.find_element_by_xpath('path')
    driver.execute_script("arguments[0].scrollIntoView();",Element)
3. Scroll to end of page:
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
4. Horizontal scroll:
'''

time.sleep(3)
driver.quit()
