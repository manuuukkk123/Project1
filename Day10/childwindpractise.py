import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
W1 = driver.window_handles
driver.switch_to.window(W1[1])
q1=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print(q1)
driver.switch_to.window(W1[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(q1)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("rahul")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//input[@id='terms']").click()
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger"))

