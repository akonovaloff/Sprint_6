from helpers.locators import MainPageLocators
from helpers.urls import URLs
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(URLs, MainPageLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get(URLs.MAIN_URL)
        wait(driver, 3).until(EC.visibility_of_element_located(self.SCOOTER_IMG_LOCATOR))

    def _wait_for_url_to_be(self, url):
        wait(self.driver, 3).until(EC.url_to_be(url),
                                   f"Текущий url не совпадает с ожидаемым:"
                                   f"\n\tТекущий: {self.driver.current_url}"
                                   f"\n\tОжидаемый: {url}")

    def click_on_top_order_button(self):
        self.driver.find_element(*self.TOP_ORDER_BUTTON).click()
        self._wait_for_url_to_be(URLs.ORDER_URL)

    def click_on_bottom_order_button(self):
        bottom_order_button_element = self.driver.find_element(*self.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", bottom_order_button_element)
        bottom_order_button_element.click()
        self._wait_for_url_to_be(URLs.ORDER_URL)