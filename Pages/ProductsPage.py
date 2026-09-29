from Pages.BasePage import BasePage
from Locators import ProductsLocators
from selenium.webdriver.common.by import By

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
        products = self.find_elements(ProductsLocators.products)
        assert len(products)>0
        for product in products:
            assert product.is_displayed()
        


        