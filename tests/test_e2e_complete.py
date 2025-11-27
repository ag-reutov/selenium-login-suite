# tests/test_e2e_complete.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_end_to_end_purchase_flow(driver):
    """
    Critical User Journey:
    Login -> Add Backpack -> Cart -> Checkout -> Fill Form -> Finish -> Verify Success
    """
    # 1. ARRANGE: Initialize all the robots (Page Objects)
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 2. ACT: Execute the "Money Flow"
    
    # Step A: Login
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    # Step B: Add Item & Go to Cart
    inventory_page.add_item_to_cart("backpack")
    inventory_page.go_to_cart()
    
    # Step C: Verify Item is in Cart & Click Checkout
    assert "Sauce Labs Backpack" in cart_page.get_cart_items()
    cart_page.click_checkout()
    
    # Step D: Fill Personal Info
    checkout_page.fill_information("Jan", "Novak", "11000")
    
    # Step E: Finish Order
    checkout_page.finish_order()
    
    # 3. ASSERT: Did we make money?
    success_msg = checkout_page.get_completion_message()
    assert "Thank you for your order!" in success_msg