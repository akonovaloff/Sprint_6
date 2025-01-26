from pages.main_page import MainPage
from helpers.urls import URLs
from conftest import driver
import allure


class TestMainPage:

    @allure.title("Проверка перехода на страницу создания заказа по верхней кнопке")
    @allure.story("Создание заказа")
    @allure.feature("Верхняя кнопка 'Заказать'")
    def test_top_order_button(self, driver):
        with allure.step("Открываем главную"):
            page = MainPage(driver)
        with allure.step("Клик по верхней кнопке 'Заказать'"):
            page.click_on_top_order_button()
        with allure.step("Проверяем, что открылась страница создания заказа"):
            assert driver.current_url == URLs.ORDER_URL

    @allure.title("Проверка перехода на страницу создания заказа по нижней кнопке")
    @allure.story("Создание заказа")
    @allure.feature("Нижняя кнопка 'Заказать'")
    def test_bottom_order_button(self, driver):
        with allure.step("Открываем главную"):
            page = MainPage(driver)
        with allure.step("Клик по нижней кнопке 'Заказать'"):
            page.click_on_bottom_order_button()
        with allure.step("Проверяем, что открылась страница создания заказа"):
            assert driver.current_url == URLs.ORDER_URL
