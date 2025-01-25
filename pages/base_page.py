import logging

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time

class BasePage:
    driver: WebDriver

    def __init__(self, driver, url):
        self.wait = None
        self.driver = driver
        self.implicitly_wait_timeout = 15
        self.explicit_wait_timeout = 60
        self.driver.implicitly_wait(self.implicitly_wait_timeout)
        self.set_explicit_wait_timeout(self.explicit_wait_timeout)
        self.driver.maximize_window()
        self.get_page(url)

    def set_explicit_wait_timeout(self, timeout: int):
        self.wait = WebDriverWait(self.driver, timeout)

    def get_page(self, url: str):
        logging.info("Open URL -> %s", url)
        self.driver.get(url)

    def quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        logging.debug("Find Element: %s", locator)
        _element = self.wait.until(ec.presence_of_element_located(locator))
        return _element

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        logging.debug("Find Element: %s", locator)
        _elements = self.wait.until(ec.presence_of_all_elements_located(locator))
        return _elements

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(0.1)
