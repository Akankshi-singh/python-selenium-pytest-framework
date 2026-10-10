import pytest
from Pages.LoginPage import LoginPage 

@pytest.mark.smoke
def test_TC006_Verify_products_are_displayed(driver, app_config):
    login_page = LoginPage(driver)

    #1. Navigate to url
    driver.get(app_config.base_url)

    #2. Login to application
    products_page = login_page.login("standard_user", "secret_sauce")

    #3. Verify products are displayed
    products_page.verify_products_are_displayed()