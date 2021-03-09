from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
#driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver = webdriver.Firefox(executable_path="D:/certificates/Selenium/Drivers/geckodriver.exe")

driver.get("http://www.demo.guru99.com/test/newtours/")

print(driver.title)           #Title of the page.

print(driver.current_url)   # Returns current url of page
print(driver.page_source)   #return HTML code for page

driver.close()          #CLose the browser
