from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

'''
1. How many input boxes present in web page
2. How to provide value into textbox
3. Get status of textbox
'''
#1.
inputBoxes = driver.find_elements(By.CLASS_NAME,'text_field')
print("Number of text input boxes: ",len(inputBoxes))

#3.
status = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print("Display Status:",status)

status = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print("Enable Status:",status)

#2.
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Raunak")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Jalan")

driver.find_element_by_id("RESULT_TextField-3").send_keys("333333")
