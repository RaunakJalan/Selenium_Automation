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


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

'''
1. Check if they are selected or not : isSelected()
2. Click on button
'''
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, "RESULT_RadioButton-7_0")))

button = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]')
driver.execute_script("arguments[0].click();", button)

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)


status = driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)
status = driver.find_element_by_id("RESULT_CheckBox-8_6").is_selected()
print(status)

# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, "RESULT_RadioButton-7_0")))

button = driver.find_element_by_xpath('//*[@id="RESULT_CheckBox-8_0"]')
driver.execute_script("arguments[0].click();", button)

button = driver.find_element_by_xpath('//*[@id="RESULT_CheckBox-8_6"]')
driver.execute_script("arguments[0].click();", button)

status = driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status)
status = driver.find_element_by_id("RESULT_CheckBox-8_6").is_selected()
print(status)



time.sleep(5)
driver.quit()
