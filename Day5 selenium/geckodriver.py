import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/KManu1/.cache/selenium/geckodriver/win64/0.33.0/geckodriver.exe")
driver = webdriver.Firefox(service = service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
time.sleep(10)
print(driver.title)
print(driver.current_url)
time.sleep(10)
driver.get("https://www.youtube.com/")
time.sleep(10)
driver.maximize_window()
time.sleep(10)
driver.maximize_window()
time.sleep(10)
driver.back() #going to back tab
time.sleep(10)
driver.forward()
time.sleep(10)
driver.refresh()
time.sleep(10)

chroomeDriverlocation = driver.service.path
print(chroomeDriverlocation)
driver.close()





