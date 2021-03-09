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


driver.get("http://demo.guru99.com/test/newtours/")


'''
1. How many links
2. Capture all links
3. Click on links
'''

links = driver.find_elements(By.TAG_NAME,"a")

print("Number of links: ",len(links))

c=1
for link in links:
    if len(link.text)>0:
        print("Link {0}:{1}".format(c,link.text))
    else:
        print("Link {0}:A dropdown link".format(c))
    c+=1


WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, 'REGISTER')))
# Click on the upload and wait...
#driver.find_element(By.LINK_TEXT,'REGISTER').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'REGIS').click()


time.sleep(5)
driver.quit()
