from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_clickable_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait_for_clickable_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_visible_element(locator)
        element.send_keys(text)

    def verify_current_url(self, url):
        assert self.driver.current_url == url

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)
