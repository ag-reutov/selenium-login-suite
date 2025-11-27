# pages/cart_page.py
from selenium.webdriver.common.by import By
# Add these three lines needed for the Explicit Wait fix:
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time # Ensure this is present if using WebDriverWait!

class CartPage:
    # --- LOCATORS ---
    CHECKOUT_BUTTON = (By.ID, "checkout")
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, ".cart_list .inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        """Returns a list of item names currently in the cart."""
        item_elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [item.text for item in item_elements]

    def click_checkout(self):
        """Waits for the checkout button to be clickable, then clicks it."""
        
        # 1. Initialize Explicit Wait
        wait = WebDriverWait(self.driver, 10)

        # 2. Wait for Clickable, find the element, and click in one line
        wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()