# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(20)
# driver.maximize_window()
#
# driver.get("https://www.flipkart.com/")
# head_title = driver.title
# print(head_title)
# driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
# driver.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']").send_keys(8553706125)
# driver.find_element(By.XPATH,"//button[normalize-space()='Request OTP']").click()

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Set up Chrome WebDriver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Implicit wait and maximize window
driver.implicitly_wait(10)
driver.maximize_window()

# Open Flipkart website
driver.get("https://www.flipkart.com/")
head_title = driver.title
print("Page Title:", head_title)

# Wait for the login modal to appear and interact with it
wait = WebDriverWait(driver, 20)

# Close the login modal by interacting with the close button (if exists)
try:
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")))
    close_button.click()
except:
    pass  # If the close button is not found, proceed with the login process

# Click on the login button in the page's header
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']")))
login_button.click()

# Input the mobile number in the login modal
mobile_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='_2IX_2- VJZDxU']")))
mobile_input.send_keys("8553706125")

# Click on 'Request OTP' button
otp_button = driver.find_element(By.XPATH, "//button[normalize-space()='Request OTP']")
otp_button.click()

# Wait for OTP entry (simulate delay for actual input)
time.sleep(5)

# Close the browser after execution
driver.quit()

