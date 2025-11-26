import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username, password, expected_error", 
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("standard_user", "wrong_pass", "Username and password do not match"),
        ("", "secret_sauce", "Username is required")
    ]
)
def test_login_failure_scenarios(driver, username, password, expected_error):
    """
    Verifies that appropriate error messages are displayed for invalid login attempts.
    
    Coverage:
    - Locked out users
    - Incorrect passwords
    - Empty credentials
    """
    # Arrange
    login_page = LoginPage(driver)
    login_page.load()
    
    # Act
    login_page.login(username, password)
    
    # Assert
    error_element = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    
    # Verify the error text matches expected data
    assert expected_error in error_element.text
    
    # Verify we are still on the login page (security check)
    assert "saucedemo.com" in driver.current_url


def test_standard_user_login(driver):
    """
    Verifies that a valid user can log in and is redirected to the inventory page.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url