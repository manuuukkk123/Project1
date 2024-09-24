from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.back() #going to back tab
driver.forward()
driver.refresh()
driver.close()

# service_obj = Service()
# driver = webdriver.Chrome(service = service_obj)
# driver.get("https://rahulshettyacademy.com")
# print(driver.title)
# driver.close()

# chroomeDriverlocation = driver.service.path
# print(chroomeDriverlocation)

# service_obj = Service("C:\Users\KManu1\AppData\Local\Programs\Python\Python311\Scripts")
# driver = webdriver.Chrome(service= service_obj)
# driver.get("https://rahulshettyacademy.com")