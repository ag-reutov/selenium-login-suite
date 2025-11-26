# pages/inventory_page.py

# 1. IMPORTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

class InventoryPage:
    
    # 2. Locator for the Sort Dropdown
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    # 3. Locator for Product Names
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    # --- INITIALIZER ---
    def __init__(self, driver):
        self.driver = driver

    # --- METHODS  ---

    def sort_by(self, option_text):
        """
        Selects an option from the sort dropdown based on visible text.
        Args:
            option_text (str): The exact text to select, e.g., "Name (Z to A)"
        """
        # A. Find the dropdown element using our locator
        dropdown_element = self.driver.find_element(*self.SORT_DROPDOWN)
        
        # B. Wrap the element in Selenium's 'Select' class
        # This gives us access to smart methods like .select_by_visible_text()
        select = Select(dropdown_element)
        
        # C. Select the option
        select.select_by_visible_text(option_text)

    def get_first_product_name(self):
        """
        Finds all product names on the page and returns the text of the first one.
        Returns:
            str: The name of the first product (e.g., "Sauce Labs Backpack")
        """
        # A. Find ALL elements that match the locator
        # Note the 's' in find_elements. This returns a Python LIST of elements.
        all_product_names = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        
        # B. Get the first item from the list (Index 0)
        first_product_element = all_product_names[0]
        
        # C. Return the visible text of that element
        return first_product_element.text