import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup Firefox WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.implicitly_wait(10)
driver.maximize_window()

# Open the webpage
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# Click on the link to open the new window
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

# Switch to the new window
W1 = driver.window_handles
driver.switch_to.window(W1[1])

# Extract email text from the new window
q1 = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print(q1)

# Switch back to the original window
driver.switch_to.window(W1[0])

# Fill out the login form
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(q1)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("rahul")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//input[@id='terms']").click()

# Click on the sign-in button
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

# Wait for the alert to appear
wait = WebDriverWait(driver, 20)
alert_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

# Print the alert message text
print(alert_element.text)

# Close the browser after execution
driver.quit()
