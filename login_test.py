import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("Opening browser...")
driver.get("https://www.saucedemo.com/")
time.sleep(2)
print("Entering credentials...")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
current_url = driver.current_url

if "inventory.html" in current_url:
    print("TEST PASSED: Login successful!")
else:
    print("TEST FAILED: Login did not redirect correctly.")

driver.quit()    