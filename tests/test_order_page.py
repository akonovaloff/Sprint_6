import allure
import pytest

from pages.order_page import OrderPage
from helpers.locators import OrderPageLocators
from conftest import driver
from helpers.urls import URLs
from selenium.webdriver.support import expected_conditions as EC
from helpers.generators import random_name, random_surname, random_address, random_phone

class TestOrderPage:

    @pytest.mark.repeat(2)
    @allure.title("Позитивное тестирование процесса создания заказа")
    @allure.feature("Страница создания заказа")
    @allure.story("Создание заказа")
    def test_order_page(self, driver):

        name = random_name()
        surname = random_surname()
        address = random_address()
        phone = random_phone()

        page = OrderPage(driver)
        page.set_name(name)
        page.set_surname(surname)
        page.set_address(address)
        page.set_phone(phone)
        page.select_random_metro_station()
        page.click_confirm_button()
        page.set_delivery_date()
        page.set_random_rental_period()
        page.set_random_color_option()

        with allure.step(f"Подтверждаю создание заказа"):
            page.click_confirm_button()
            page.click_confirm_button()
            success_form_element = page.find_element(OrderPageLocators.SUCCESS_ORDER_INFORMATION_LOCATOR)
            assert success_form_element.is_displayed()

        with allure.step(f"Получаю номер заказа"):
            order_number = page.get_order_number()

    @allure.title("Тест перехода по клику на логотип Яндекс")
    @allure.feature("Логотип Яндекс")
    def test_click_on_yandex_logo(self, driver):
        with allure.step(f"Открываю страницу {URLs.MAIN_URL}"):
            page = OrderPage(driver)

        with allure.step("Проверка перехода на главную страницу dzen"):
            page.click_yandex_logo()
            driver.switch_to.window(window_name=driver.window_handles[1])
            page.wait.until(EC.url_contains('dzen'), "Адрес страницы на новой вкладке не содержит 'dzen'")
            assert "dzen" in driver.current_url, "Адрес страницы на новой вкладке не содержит 'dzen'"
            driver.close()
            driver.switch_to.window(window_name=driver.window_handles[0])

    @allure.title("Тест перехода по клику на логотип Самокат")
    @allure.feature("Логотип Самокат")
    def test_click_on_samokat_logo(self, driver):
        with allure.step(f"Открываю страницу создания заказа"):
            page = OrderPage(driver)

        with allure.step("Проверка перехода на главную страницу samokat"):
            page.click_samokat_logo()
