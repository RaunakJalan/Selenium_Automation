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
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

time.sleep(5)
admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgnt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()




time.sleep(5)
driver.quit()
