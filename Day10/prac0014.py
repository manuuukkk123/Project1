# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
#
# # Set up Chrome WebDriver using webdriver-manager
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
# # Implicit wait and maximize window
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# # Open Flipkart website
# driver.get("https://www.flipkart.com/")
# head_title = driver.title
# print("Page Title:", head_title)
#
# # Wait for the login modal to appear and interact with it
# wait = WebDriverWait(driver, 30)
#
# # Close the login modal by interacting with the close button (if exists)
# try:
#     close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")))
#     close_button.click()
#     print("Closed login modal")
# except Exception as e:
#     print("Login modal close button not found:", str(e))
#
# # Perform mouse hover on the login button in the page's header
# try:
#     login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Login']")))
#     actions = ActionChains(driver)
#     actions.move_to_element(login_button).perform()  # Perform mouse hover
#     print("Hovered over the login button")
# except Exception as e:
#     print("Login button not found:", str(e))
#
# # Navigate to 'Mobiles' section by clicking on the Mobiles image
# try:
#     mobiles_image = driver.find_element(By.XPATH, "//img[@alt='Mobiles']")
#     mobiles_image.click()
#     print("Navigated to Mobiles section")
# except Exception as e:
#     print("Mobiles section not found:", str(e))
#
# # Select Apple checkbox
# try:
#     apple_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Apple']//div[@class='XqNaEv']")))
#     apple_checkbox.click()
#     print("Apple checkbox selected")
# except Exception as e:
#     print("Apple checkbox not found:", str(e))
#
# # Select iPhone 15 product and add to cart
# try:
#     iphone15 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='KzDlHZ'  and text()='Apple iPhone 15 (Blue, 128 GB)']")))
#     iphone15.click()
#     print("iPhone 15 selected")
#
#     # Wait for the Add to Cart button and click it
#     add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/button[1]")))
#     add_to_cart.click()
#     print("iPhone 15 added to cart")
#
# except Exception as e:
#     print("Error adding iPhone to cart:", str(e))
#
# # Navigate to Cart
# try:
#     flipkart_logo = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Flipkart']")))
#     flipkart_logo.click()
#     cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Cart']")))
#     cart_button.click()
#     print("Navigated to Cart")
#
#     # Click on the remove item button (Adjust the selector if needed)
#     remove_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_3dsJAO']")))  # Assuming it's the remove button
#     remove_item.click()
#     print("Item removed from cart")
# except Exception as e:
#     print("Error navigating to cart or removing item:", str(e))
#
# # Wait for OTP entry (simulate delay for actual input)
# time.sleep(5)
#
# # Close the browser after execution
# driver.quit()

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

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

# Perform mouse hover on the login button in the page's header
try:
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Login']")))
    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()  # Perform mouse hover
    print("Hovered over the login button")
except Exception as e:
    print("Login button not found:", str(e))

# Navigate to 'Mobiles' section by clicking on the Mobiles image
try:
    mobiles_image = driver.find_element(By.XPATH, "//img[@alt='Mobiles']")
    mobiles_image.click()
    print("Navigated to Mobiles section")
except Exception as e:
    print("Mobiles section not found:", str(e))

# Select Apple checkbox
try:
    apple_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Apple']//div[@class='XqNaEv']")))
    apple_checkbox.click()
    print("Apple checkbox selected")
except Exception as e:
    print("Apple checkbox not found:", str(e))

# Select iPhone 15 product and add to cart
try:
    iphone15 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Apple iPhone 15 (Blue, 128 GB)']")))
    iphone15.click()
    print("iPhone 15 selected")

    # Wait for the Add to Cart button and click it
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']")))
    add_to_cart.click()
    print("iPhone 15 added to cart")

except StaleElementReferenceException:
    # Retry fetching the element if a stale reference occurs
    print("Stale element reference - retrying...")
    iphone15 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Apple iPhone 15 (Blue, 128 GB)']")))
    iphone15.click()
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']")))
    add_to_cart.click()
    print("iPhone 15 added to cart after retry")

except Exception as e:
    print("Error adding iPhone to cart:", str(e))

# Navigate to Cart
try:
    flipkart_logo = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Flipkart']")))
    flipkart_logo.click()

    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Cart']")))
    cart_button.click()
    print("Navigated to Cart")

    # Wait for and click on the remove item button (adjust the selector if needed)
    remove_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_3dsJAO']")))  # Assuming it's the remove button
    remove_item.click()
    print("Item removed from cart")
except StaleElementReferenceException:
    # Retry in case of stale element reference
    print("Stale element reference in Cart - retrying...")
    flipkart_logo.click()
    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Cart']")))
    cart_button.click()
    remove_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_3dsJAO']")))
    remove_item.click()
    print("Item removed from cart after retry")
except Exception as e:
    print("Error navigating to cart or removing item:", str(e))

# Wait for OTP entry (simulate delay for actual input)
time.sleep(5)

# Close the browser after execution
driver.quit()

