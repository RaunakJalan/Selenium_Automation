from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)           #Title of the page.

print(driver.current_url)   # Returns current url of page
#print(driver.page_source)   #return HTML code for page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)

#driver.close()          #CLose the tab one at a time
driver.quit()           #Closes all tabs at once
