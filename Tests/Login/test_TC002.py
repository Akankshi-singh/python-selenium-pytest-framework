import pytest
from Pages.LoginPage import LoginPage

@pytest.mark.parametrize("username, password", 
                         [("wrong_user", "secret_sauce"),
                          ("standard_user", "wrong_password")])

def test_TC002(driver, username, password):
    
    #TC-002 Login with invalid username & password/ valid username & invalid password
    login_page = LoginPage(driver)

    # 1. navigate to URL
    driver.get("https://www.saucedemo.com/")

    #2. Enter Username, Password and click login
    login_page.enter_username(username) 
    login_page.enter_password(password)
    login_page.click_login()

    #3. Verify that error message is displayed
    assert login_page.error_message_displayed()