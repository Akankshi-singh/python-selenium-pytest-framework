from selenium import webdriver
from Pages.LoginPage import LoginPage

def test_TC008_sort_products_low_to_high():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    #1. Navigate to URL
    driver.get("https://www.saucedemo.com/")

    #2. Login
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Click sort button and apply Low to High sort filter
    products_page.sort_dropdown("Price (low to high)")

    #4. Verify that products are sorted
    products_page.verify_items_are_sorted_low_to_high()





