#Implicit wait  -
#Explicit Wait
import time

from selenium import webdriver
#pause the test for few seconds using Time class
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []
service_obj=Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/116.0.5845.96/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(4)
driver.find_element(By.XPATH,"//div[@class='products']/div")
buttons = driver.find_element(By.XPATH,"//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list.append(driver.find_element(By.XPATH,"parent::div/parent::div/h4")).text
    button.click()
print(list)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
# wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME,"promoCode"))
veggies =driver.find_element(By.CSS_SELECTOR,"p.product-name")
for veg in veggies:
    list2.append(veg.text)

print(list2)
assert list == list2
originalAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
discountAmount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text

assert float(discountAmount) < int(originalAmount)

print(driver.find_element(By.CSS_SELECTOR,"span.promoInfo").text)

amounts = driver.find_element(By.XPATH,"//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text) #32+48+60

print(sum)

totalAmount = float(driver.find_element(By.CLASS_NAME,"totAmt").text)

assert sum == totalAmount





