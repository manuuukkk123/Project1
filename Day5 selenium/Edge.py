from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/KManu1/.cache/selenium/msedgedriver/win64/116.0.1938.62/msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.back() #going to back tab
driver.forward()
driver.refresh()
chroomeDriverlocation = driver.service.path
print(chroomeDriverlocation)
driver.close()