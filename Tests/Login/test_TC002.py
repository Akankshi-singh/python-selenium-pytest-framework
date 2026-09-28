from selenium import webdriver
from Pages.LoginPage import LoginPage

def test_TC002():
    driver = webdriver.Chrome()

    #TC-002 Login with invalid username & password
    login_page = LoginPage(driver)

    # 1. navigate to URL
    driver.get("https://www.saucedemo.com/")

    #2. Enter Username, Password and click login
    login_page.enter_username("wrong_user") 
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    #3. Verify that error message is displayed
    assert login_page.error_message_displayed()