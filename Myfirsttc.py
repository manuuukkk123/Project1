from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
# driver.find_element(By.ID,"txtPassword").send_keys("admin123")
# driver.find_element(By.ID,"btnLogin").click()