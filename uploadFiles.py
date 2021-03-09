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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D://IMAGES AND VIDEOS PHONE/test.jpg")
time.sleep(5)
driver.quit()
