import pytest
from selenium import webdriver
from configuration import config

@pytest.fixture
def driver():
    browser = config.browser.lower()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    yield driver
    driver.quit()

    