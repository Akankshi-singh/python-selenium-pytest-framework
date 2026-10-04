from selenium import webdriver
from Pages.LoginPage import LoginPage

def test_TC009_match_product_name_and_price(driver):
    login_page = LoginPage(driver)

    #1. Navigate to URL
    driver.get("https://www.saucedemo.com/")

    #2. Login
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Get product name
    product_name_on_inventory_page= products_page.get_product_name("Sauce Labs Bolt T-Shirt")

    #4. Get product price
    product_price_on_inventory_page=products_page.get_product_price("Sauce Labs Bolt T-Shirt")

    #5. Click on a product
    products_page.click_item_on_products_page("Sauce Labs Bolt T-Shirt")

    #6. Get product name on product details page 
    product_name_on_product_details = products_page.product_name_on_product_page("Sauce Labs Bolt T-Shirt")

    #7. Get price on product details page 
    product_price_on_product_details = products_page.verify_price_on_product_details_page("Sauce Labs Bolt T-Shirt")

    #5. Verify product name
    assert product_name_on_inventory_page == product_name_on_product_details
    assert product_price_on_inventory_page == product_price_on_product_details

