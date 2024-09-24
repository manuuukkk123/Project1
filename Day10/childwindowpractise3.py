import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
message= driver.find_element(By.CSS_SELECTOR,".red").text
var = message.split("at")[1].strip().split(" ")[0]
print(var)
driver.close()
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 20)
alert_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(alert_element.text)
driver.close()
