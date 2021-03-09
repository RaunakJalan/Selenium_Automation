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

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame('packageListFrame')
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()


time.sleep(3)
driver.quit()
