import pytest
from selenium import webdriver
from configuration import config

@pytest.fixture
def driver():
    browser = config.browser.lower()
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if config.headless == True:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if config.headless == True:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "safari":
        options = webdriver.SafariOptions()
        if config.headless == True:
            options.add_argument("--headless")
        driver = webdriver.Safari(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    yield driver
    driver.quit()

    