from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


'''
1. Select one option: 3 options
2. Find out what options in drop down
3. Count number of options in drop down
'''
element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

#select by visible text
#drp.select_by_visible_text('Morning') #Morning

#select by index
#drp.select_by_index(2)   #Afternoon

#select by value
drp.select_by_value("Radio-2")   #Evening

#3.
print(len(drp.options))

# 2.
all_options = drp.options

for option in all_options:
    print(option.text)






time.sleep(5)
driver.quit()
