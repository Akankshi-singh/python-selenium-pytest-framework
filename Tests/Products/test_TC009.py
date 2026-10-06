import pytest
from Pages.LoginPage import LoginPage

@pytest.mark.parametrize("product",
                         ["Sauce Labs Bolt T-Shirt",
                           "Sauce Labs Backpack",
                           "Sauce Labs Bike Light"])

@pytest.mark.regression
def test_TC009_match_product_name_and_price(driver, product):
    login_page = LoginPage(driver)

    #1. Navigate to URL
    driver.get("https://www.saucedemo.com/")

    #2. Login
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Get product name
    product_name_on_inventory_page= products_page.get_product_name(product)

    #4. Get product price
    product_price_on_inventory_page=products_page.get_product_price(product)

    #5. Click on a product
    products_page.click_item_on_products_page(product)

    #6. Get product name on product details page 
    product_name_on_product_details = products_page.product_name_on_product_page(product)

    #7. Get price on product details page 
    product_price_on_product_details = products_page.verify_price_on_product_details_page(product)

    #5. Verify product name
    assert product_name_on_inventory_page == product_name_on_product_details
    assert product_price_on_inventory_page == product_price_on_product_details

