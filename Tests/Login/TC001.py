from selenium import webdriver
from Pages import LoginPage

driver = webdriver.Chrome()
login_page = LoginPage(driver)

##TC001: Login with valid username and password

#1.Navigate to the sauce demo application
driver.get("https://www.saucedemo.com/")

#2.Enter Username, password and click on login button
products_page = login_page.login("standard_user", "secret_sauce")

#3.Verify the title 
products_page.verify_products_title("Products")

