from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj=Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/116.0.5845.96/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsopened=driver.window_handles
driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsopened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
