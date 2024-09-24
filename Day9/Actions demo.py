import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
service_obj = Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/116.0.5845.96/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action=ActionChains(driver)
# action.double_click(driver.find_element(By))
# action.context_click() # Right click
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# driver.implicitly_wait(100)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
action.double_click(driver.find_element(By.ID,"checkBoxOption1")).perform()
driver.implicitly_wait(100)
action.context_click(driver.find_element(By.LINK_TEXT,"Open Tab")).click().perform()
time.sleep(50)