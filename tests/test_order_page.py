import allure
import pytest

from pages.order_page import OrderPage
from conftest import driver
from helpers.urls import URLs
import random
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestOrderPage:

    @pytest.mark.repeat(2)
    @allure.title("Позитивное тестирование процесса создания заказа")
    @allure.feature("Страница создания заказа")
    @allure.story("Создание заказа")
    def test_order_page(self, driver):
        NAMES = ["Ахилл", "Одиссей", "Агамемнон", "Гектор", "Парис", "Патрокл", "Приам"]
        SURNAMES = ["Великий", "Мудрый", "Прекрасный", "Ясноликий", "Первый", "Последний", "Синий"]
        ADDRESSES = ["Москва", "Санкт-Петербург", "Екатеринбург", "Бобруйск", "деревня Тушино"]

        name = random.choice(NAMES)
        surname = random.choice(SURNAMES)
        address = random.choice(ADDRESSES)
        phone = str(random.randint(10000000000, 99999999999))

        with allure.step(f"Открываю страницу {URLs.MAIN_URL}"):
            page = OrderPage(driver)



        with allure.step("Возврат на страницу заказа"):
            driver.get(URLs.ORDER_URL)
            time.sleep(1)

        with allure.step(f"Ввожу имя: {name}"):
            page.set_name(name)

        with allure.step(f"Ввожу фамилию: {surname}"):
            page.set_surname(surname)

        with allure.step(f"Ввожу адрес: {address}"):
            page.set_address(address)

        with allure.step(f"Ввожу телефон: {phone}"):
            page.set_phone(phone)

        with allure.step(f"Выбираю станцию метро"):
            page.select_random_metro_station()

        with allure.step(f"Нажимаю кнопку подтверждения"):
            page.click_confirm_button()

        with allure.step(f"Выбираю дату доставки"):
            page.set_delivery_date()

        with allure.step(f"Выбираю срок аренды"):
            page.set_random_rental_period()

        with allure.step(f"Выбираю цвет"):
            page.set_random_color_option()

        with allure.step(f"Нажимаю кнопку подтверждения"):
            page.click_confirm_button()
            page.click_confirm_button()
            success_form_element = driver.find_element(*OrderPage.SUCCESS_ORDER_INFORMATION_LOCATOR)
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
            wait(driver, 3).until(EC.url_contains('dzen'), "Адрес страницы на новой вкладке не содержит 'dzen'")
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