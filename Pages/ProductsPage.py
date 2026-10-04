from Pages.BasePage import BasePage
from Locators import ProductsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class ProductsPage(BasePage):

    def verify_products_title(self, title):
        element = self.wait_for_visible_element(ProductsLocators.products_title)
        assert element.text == title

    # def add_product_to_cart(self, product_name):
    #     product_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
    #     locator = (By.ID, product_id)
    #     self.click(locator)

    def add_product_to_cart(self, product_name):
        locator = (ProductsLocators.add_to_cart_button[0],
                   ProductsLocators.add_to_cart_button[1].format(product_name = product_name))
        self.click(locator)

    def click_item_on_products_page(self, product_name):
        locator = (ProductsLocators.items_on_products_page[0],
                   ProductsLocators.items_on_products_page[1].format(product_name = product_name))
        self.click(locator)

    def verify_products_are_displayed(self):
        items = self.get_elements(ProductsLocators.items)
        assert len(items)>0, "No items are displayed on the products page"

        for item in items:
            assert item.is_displayed()

    def sort_dropdown(self, text):
        sort_dropdown = self.wait_for_visible_element(ProductsLocators.sort_button)
        options = Select(sort_dropdown)
        options.select_by_visible_text(text)

    def verify_items_are_sorted_low_to_high(self):
        prices = self.get_elements(ProductsLocators.items_price)
        i = 0
        for i in range(i, len(prices)):
            for j in range(i+1, len(prices)):
                price_i =float(prices[i].text.replace("$", ""))
                price_j =float(prices[j].text.replace("$", ""))
                assert price_i<=price_j , "Items are not sorted properly"

    def get_shopping_cart_badge(self):
        shopping_cart_badge = self.wait_for_visible_element(ProductsLocators.shopping_cart_badge)
        badge_value = shopping_cart_badge.text
        return int(badge_value)

    def verify_shopping_cart_badge_updates(self, product_name1,product_name2 ):
        self.add_product_to_cart(product_name1)
        badge_value = self.get_shopping_cart_badge()
        self.add_product_to_cart(product_name2)
        updated_value = self.get_shopping_cart_badge()
        assert updated_value == badge_value+1, "Shopping cart badge is not updated"

    def product_name_on_product_page(self, product_name):
        locator = (ProductsLocators.product_name_on_product_details[0],
                   ProductsLocators.product_name_on_product_details[1].format(product_name = product_name))
        element = self.wait_for_visible_element(locator)
        return element.text

    def verify_price_on_product_details_page(self, product_name):
        locator = (ProductsLocators.price_on_product_details[0],
                   ProductsLocators.price_on_product_details[1].format(product_name = product_name))
        element = self.wait_for_visible_element(locator)
        return element.text

    def get_product_price(self, product_name):
        locator = (ProductsLocators.product_price[0],
                   ProductsLocators.product_price[1].format(product_name=product_name))
        element = self.wait_for_visible_element(locator)
        return element.text

    def get_product_name(self, product_name):
        locator = (ProductsLocators.items_on_products_page[0],
                   ProductsLocators.items_on_products_page[1].format(product_name = product_name))
        element = self.wait_for_visible_element(locator)
        return element.text

    




        