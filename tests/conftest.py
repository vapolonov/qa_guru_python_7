from selene.support.shared import browser
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # browser.config.base_url = 'https://github.com'
    # browser.config.browser_name = 'chrome'
    # browser.config.timeout = 3
    # browser.config.window_width = 1920
    # browser.config.window_height = 1024
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = options
    yield browser
    browser.quit()
