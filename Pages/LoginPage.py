from Locators import LoginLocators
from Pages.BasePage import BasePage
from Pages.ProductsPage import ProductsPage

class LoginPage(BasePage):

    def get_username_field(self):
        return self.wait_for_visible_element(LoginLocators.username_input)

    def get_password_field(self):
        return self.wait_for_visible_element(LoginLocators.password_input)

    def get_login_button(self):
        return self.wait_for_visible_element(LoginLocators.login_button)

    def get_credentials_container(self):
        return self.wait_for_visible_element(LoginLocators.credentials_container)

    def enter_username(self, username):
        return self.enter_text(LoginLocators.username_input, username)

    def enter_password(self, password):
        return self.enter_text(LoginLocators.password_input, password)

    def click_login(self):
        self.click(LoginLocators.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return ProductsPage(self.driver)

    def error_message_displayed(self):
        return self.wait_for_visible_element(LoginLocators.error_message)

    def empty_field_error_displayed(self):
        return self.wait_for_visible_element(LoginLocators.empty_fields_error)

    

    