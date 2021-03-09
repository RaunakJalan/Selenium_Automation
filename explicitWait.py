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

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.expedia.com/")
time.sleep(5)
#driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()   #click on flight button

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")   #fill origin city
time.sleep(2)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")   #fill destination city

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("08/01/2020")   #fill departing date

driver.find_element(By.ID, "flight-returning-hp-flight").clear()   #mm/dd/yyyy
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("08/04/2020")   #fill returning date

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

#Explicit Waits
wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(20)

driver.quit()
