import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get("https://www.google.com")
# print(driver.title)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"//input[@id='checkBoxOption1']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break
#Radio butoon
radiobutton = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
radiobutton[2].click()
assert radiobutton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


time.sleep(20)
driver.quit()

