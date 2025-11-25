# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Setup: Initializes the Chrome browser
    print("\nStarting browser...")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
    yield driver

    # Teardown: Quits the browser after all tests in the module are done
    print("\nQuitting browser...")
    driver.quit()