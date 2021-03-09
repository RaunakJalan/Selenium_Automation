from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time

options = Options()
options.add_experimental_option('prefs', {
    "download.default_directory":"D:\certificates\Selenium",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True})
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
driver_path = 'D:/certificates/Selenium/Drivers/chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# text file
driver.find_element_by_id("textbox").send_keys("testing download of text file")
driver.find_element_by_id("createTxt").click()
time.sleep(3)
driver.find_element_by_id("link-to-download").click()

#pdf Files
# text file
driver.find_element_by_id("pdfbox").send_keys("testing download of pdf file")
driver.find_element_by_id("createPdf").click()
time.sleep(3)
driver.find_element_by_id("pdf-link-to-download").click()






time.sleep(5)
driver.quit()
