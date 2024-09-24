from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chrome_options)


servce_obj = Service("C:/Users/KManu1/.cache/selenium/chromedriver/win64/116.0.5845.96/chromedriver.exe")
driver=webdriver.Chrome(service=servce_obj,options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)