import pytest
from Pages.LoginPage import LoginPage

@pytest.mark.smoke
def test_TC005_Verify_Products_page_URL_after_successful_login(driver):
    login_page = LoginPage(driver)

    #1. Navigate to URL
    driver.get("https://www.saucedemo.com/")

    #2. Login to the application (Enter username, password and click login)
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Verify the URL
    products_page.verify_current_url("https://www.saucedemo.com/inventory.html")