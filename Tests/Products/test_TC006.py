from selenium import webdriver
from Pages.LoginPage import LoginPage 

def test_TC006_Verify_products_are_displayed():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    #1. Navigate to url
    driver.get("https://www.saucedemo.com/")

    #2. Login to application
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Verify products are displayed
    products_page.verify_products_are_displayed()