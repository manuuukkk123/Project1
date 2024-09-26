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
wait = WebDriverWait(driver, 30)

# Close the login modal by interacting with the close button (if exists)
try:
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")))
    close_button.click()
    print("Closed login modal")
except Exception as e:
    print("Login modal close button not found:", str(e))

# Click on the login button in the page's header
try:
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']")))
    login_button.click()
    print("Login button clicked")
except Exception as e:
    print("Login button not found:", str(e))

# Input the mobile number in the login modal
try:
    mobile_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[class='r4vIwl BV+Dqf']")))
    mobile_input.send_keys("rdltest847@gmail.com")
    print("Mobile number entered")
except Exception as e:
    print("Mobile input field not found or not visible:", str(e))

# Click on 'Request OTP' button
try:
    otp_button = driver.find_element(By.XPATH, "//button[normalize-space()='Request OTP']")
    otp_button.click()
    print("OTP request button clicked")
except Exception as e:
    print("OTP request button not found:", str(e))




# Wait for OTP entry (simulate delay for actual input)
time.sleep(5)

# Close the browser after execution
driver.quit()
