from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies=[]
servce_obj = Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/116.0.5845.96/chromedriver.exe")
driver=webdriver.Chrome(service=servce_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all veggie names --->BrowserSortedveggielist9A,B,C)
veggieWebElements=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalbrowsersortedlist = browserSortedVeggies.copy()
# Sort this Browsersortedveggielist --->newsortedlist-->(A,B,C)
browserSortedVeggies.sort()

assert browserSortedVeggies == originalbrowsersortedlist