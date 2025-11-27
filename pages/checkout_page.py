# pages/checkout_page.py
from selenium.webdriver.common.by import By

class CheckoutPage:
    # --- LOCATORS ---
    # Input fields for the user form
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    # Final confirmation steps
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header") # The "Thank You" H2 tag

    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first, last, zip_code):
        """Fills the inputs and submits the form."""
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_order(self):
        """Clicks the final finish button."""
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_completion_message(self):
        """Returns the text of the success header."""
        return self.driver.find_element(*self.COMPLETE_HEADER).text