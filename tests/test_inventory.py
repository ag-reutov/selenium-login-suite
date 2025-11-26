# tests/test_inventory.py

# 1. IMPORTS
# We need the LoginPage to get into the system.
from pages.login_page import LoginPage
# We need the InventoryPage to interact with the products and sorting.
from pages.inventory_page import InventoryPage

def test_sort_products_z_to_a(driver):
    """
    Verifies that selecting 'Name (Z to A)' from the sort dropdown
    correctly reorders the product list.
    """
    
    # 2. ARRANGE 
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    # Perform the login steps to reach the inventory page.
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    # 3. ACT 
    inventory_page.sort_by("Name (Z to A)")
    
    # 4. ASSERT 
    expected_first_item = "Test.allTheThings() T-Shirt (Red)"
    
    # Get the actual first item from the browser using our helper method.
    actual_first_item = inventory_page.get_first_product_name()
    
    # Compare them. If they don't match, the test fails with our custom error message.
    assert actual_first_item == expected_first_item, \
        f"Sorting failed! Expected '{expected_first_item}' but got '{actual_first_item}'"