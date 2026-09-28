from selenium import webdriver
from Pages.LoginPage import LoginPage

def test_TC004():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)

    #TC-004 Verify login page elements

    #1. Navigate to the URL
    driver.get("https://www.saucedemo.com/")

    #2. Verify username field is displayed
    username = login_page.get_username_field()
    assert username.is_displayed()

    #3. Verify password field is displayed
    password = login_page.get_password_field()
    assert password.is_displayed()

    #4. Verify login button is displayed
    login= login_page.get_login_button()
    assert login.is_displayed()

    #5. Verify credentials container is displayed
    credentials_container = login_page.get_credentials_container()
    assert credentials_container.is_displayed()