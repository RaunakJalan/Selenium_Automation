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

driver.get("file:///D:/certificates/Selenium/tableHtml.html")


rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("Rows:{0}, Columns:{1}".format(rows, cols))

print("\n")
print("Product \tArticle  Price")
print("-"*30)
for r in range(2,rows+1):
    for c in range(1, cols+1):
        xpath = "/html/body/table/tbody/tr[{0}]/td[{1}]".format(r,c)
        data = driver.find_element_by_xpath(xpath)
        print(data.text,end="\t")
    print("\n")





time.sleep(3)
driver.quit()
