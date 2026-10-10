import pytest
from Pages.LoginPage import LoginPage

@pytest.mark.regression
def test_TC003(driver, app_config):

    login_page = LoginPage(driver)

    #TC003-Login with blank username and password

    #1. Navigate to URL
    driver.get(app_config.base_url)

    #2. Click login
    login_page.click_login()

    #3. Verify the error message
    assert login_page.empty_field_error_displayed()