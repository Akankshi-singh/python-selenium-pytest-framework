from Locators import LoginLocators
from Pages import BasePage
from Pages import ProductsPage

class LoginPage(BasePage):

    def enter_username(self, username):
        self.enter_text(LoginLocators.username_input, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.password_input, password)

    def click_login(self):
        self.click(LoginLocators.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return ProductsPage(self.driver)