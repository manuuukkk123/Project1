import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/116.0.5845.96/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, XPATH, CSSSelector, Classname, name, LinkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()

#Xpath Syntax --> //tagname[@attribute = 'value']  --->EX //input[@type ='submit']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

time.sleep(10)