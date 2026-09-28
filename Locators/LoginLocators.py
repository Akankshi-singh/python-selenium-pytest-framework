from selenium.webdriver.common.by import By

username_input = (By.XPATH, "//input[@id='user-name']")
password_input = (By.XPATH, "//input[@id='password']")
login_button = (By.XPATH, "//input[@id='login-button']")
error_message = (By.XPATH, "//h3[@data-test='error' and contains(., 'Epic sadface: Username and password do not match any user in this service')]")
empty_fields_error = (By.XPATH, "//h3[@data-test='error' and contains(., 'Epic sadface: Username is required')]")
credentials_container = (By.XPATH, "//div[@data-test='login-credentials-container']")