import pytest
from Pages.LoginPage import LoginPage

@pytest.mark.smoke
def test_TC008_verify_shopping_cart_badge_updates(driver, app_config):
    login_page = LoginPage(driver)

    #1. Navigate to URL
    driver.get(app_config.base_url)

    #2. Login to the application
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Verify that the Shopping cart badge updated on adding products to cart
    products_page.verify_shopping_cart_badge_updates(product_name1 = "Sauce Labs Backpack", product_name2 = "Sauce Labs Bike Light")