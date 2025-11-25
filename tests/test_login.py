# tests/test_login.py
from pages.login_page import LoginPage

def test_standard_user_login(driver):
    # 1. Arrange: Initialize the page and load the site
    login_page = LoginPage(driver)
    login_page.load()

    # 2. Act: Perform the login action
    login_page.login("standard_user", "secret_sauce")

    # 3. Assert: Verify the URL change
    assert "inventory.html" in driver.current_url