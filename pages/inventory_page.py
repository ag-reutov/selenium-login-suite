# pages/inventory_page.py

# IMPORTS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

class InventoryPage:
    
   
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def go_to_cart(self):
        """Finds the cart icon and uses JavaScript to force the click, ensuring navigation."""
        
        CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
        
        # 1. Find the element (The cart icon object)
        cart_icon = self.driver.find_element(*CART_LINK)
        
        # 2. Execute JavaScript Click: This is the most reliable way to ensure a click registers.
        self.driver.execute_script("arguments[0].click();", cart_icon)

  
    def __init__(self, driver):
        self.driver = driver
    
    def add_item_to_cart(self, item_name="backpack"):
        """Clicks the button to add a specific item (default: backpack) to the cart."""
        
        # We define the specific locator for the backpack item
        ADD_TO_CART_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
        
        # For simplicity, we only handle the backpack for this test
        if item_name == "backpack":
            self.driver.find_element(*ADD_TO_CART_BACKPACK_BUTTON).click()
        else:
            raise NotImplementedError(f"Adding item {item_name} not yet implemented.")

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