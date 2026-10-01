from selenium.webdriver.common.by import By
from Pages import ProductsPage

products_title = (By.XPATH, "//span[@class='title' and text() = 'Products']")
add_to_cart_button = (By.XPATH, "//div[@data-test='inventory-item-name' and text() = '{product_name}']/ancestor::div[@class='inventory_item']//button[text()= 'Add to cart']")
items_on_products_page = (By.XPATH, "//div[@data-test='inventory-item-name' and text() = '{product_name}']")
shopping_cart_link = (By.XPATH, "//a[@data-test='shopping-cart-link']")
sort_button = (By.XPATH, "//select[@data-test='product-sort-container']")
items = (By.XPATH, "//div[@class='inventory_item']")
sort_button = (By.XPATH, "//select[@class='product_sort_container']")
items_price = (By.XPATH, "//div[@class='inventory_item_price' and contains(., '$')]")
shopping_cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge' and contains(., '')]")