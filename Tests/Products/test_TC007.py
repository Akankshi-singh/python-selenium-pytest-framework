import pytest
from Pages.LoginPage import LoginPage

@pytest.mark.regression
def test_TC007_sort_products_low_to_high(driver, app_config):
    login_page = LoginPage(driver)

    #1. Navigate to URL
    driver.get(app_config.base_url)

    #2. Login
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Click sort button and apply Low to High sort filter
    products_page.sort_dropdown("Price (low to high)")

    #4. Verify that products are sorted
    products_page.verify_items_are_sorted_low_to_high()





