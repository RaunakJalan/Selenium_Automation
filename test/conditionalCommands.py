from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://www.demo.guru99.com/test/newtours/")

user_ele = driver.find_element_by_name("userName")

print(user_ele.is_displayed())  #True/False based on visibility of element

print(user_ele.is_enabled())    #True/False based on status of element


pass_ele = driver.find_element_by_name("password")
print(pass_ele.is_displayed())  #True/False based on visibility of element

print(pass_ele.is_enabled())    #True/False based on status of element

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

driver.find_element_by_name("submit").click()
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("roundtrip radio: ",roundtrip_radio.is_selected())

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("onetrip radio: ",onetrip_radio.is_selected())


#driver.quit()           #Closes all tabs at once
