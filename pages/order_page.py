from selenium.webdriver.remote.webdriver import WebDriver
from helpers.locators import OrderPageLocators
from helpers.urls import URLs
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import allure
import time

class OrderPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver, URLs.ORDER_URL)
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))

    def set_name(self, name: str):
        with allure.step(f"Ввожу имя: {name}"):
            name_field_locator = OrderPageLocators.NAME_FIELD_LOCATOR
            name_field_element = self.find_element(name_field_locator)
            name_field_element.send_keys(name)

    def set_surname(self, surname: str):
        with allure.step(f"Ввожу фамилию: {surname}"):
            surname_field_locator = OrderPageLocators.SURNAME_FIELD_LOCATOR
            surname_field_element = self.find_element(surname_field_locator)
            surname_field_element.send_keys(surname)

    def set_address(self, address: str):
        with allure.step(f"Ввожу адрес: {address}"):
            address_field_locator = OrderPageLocators.ADDRESS_FIELD_LOCATOR
            address_field_element = self.find_element(address_field_locator)
            address_field_element.send_keys(address)

    def set_phone(self, phone: str):
        with allure.step(f"Ввожу телефон: {phone}"):
            phone_field_locator = OrderPageLocators.PHONE_FIELD_LOCATOR
            phone_field_element = self.find_element(phone_field_locator)
            phone_field_element.send_keys(phone)

    def click_confirm_button(self):
        with allure.step(f"Нажимаю кнопку подтверждения"):
            buttons = self.find_elements(OrderPageLocators.CONFIRM_BUTTON)
            if len(buttons) == 1:
                index = 0
            elif len(buttons) == 2:
                index = 1
            else:
                index = -1
            buttons[index].click()

            self.wait.until(
                EC.visibility_of_element_located(OrderPageLocators.DELIVERY_DATE_FIELD_LOCATOR) or
                EC.visibility_of_element_located(OrderPageLocators.ORDER_ERROR_MESSAGE_LOCATOR) or
                EC.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRMATION_FORM_LOCATOR) or
                EC.visibility_of_element_located(OrderPageLocators.SUCCESS_ORDER_INFORMATION_LOCATOR))

    def select_random_metro_station(self):
        with allure.step(f"Выбираю станцию метро"):
            self.find_element(OrderPageLocators.METRO_FIELD_LOCATOR).click()
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.METRO_STATION_SELECTOR_LOCATOR))
            metro_station_list = self.find_elements(OrderPageLocators.METRO_STATION_SELECTOR_LOCATOR)
            n = randint(0, len(metro_station_list) - 1)
            print(f"Выбрана станция метро: {metro_station_list[n].text}")
            self.scroll_to_element(metro_station_list[n])
            metro_station_list[n].click()

    def set_delivery_date(self):
        with allure.step(f"Выбираю дату доставки"):
            self.find_element(OrderPageLocators.DELIVERY_DATE_FIELD_LOCATOR).click()
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.TODAY_CALENDAR_LOCATOR))
            self.find_element(OrderPageLocators.TODAY_CALENDAR_LOCATOR).click()

    def set_random_rental_period(self):
        with allure.step(f"Выбираю срок аренды"):
            self.find_element(OrderPageLocators.RENTAL_PERIOD_FIELD_LOCATOR).click()
            self.wait.until(
                EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN_MENU_LOCATOR))
            rental_options_elements = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTIONS_LOCATOR)
            n = randint(0, len(rental_options_elements) - 1)
            rental_options_elements[n].click()

    def set_random_color_option(self):
        with allure.step(f"Выбираю цвет"):
            color_option_elements = self.find_elements(OrderPageLocators.COLOR_OPTIONS_LOCATOR)
            color_len = len(color_option_elements)
            n = randint(0, color_len - 1)
            color_option_elements[n].click()

    def get_order_number(self):
        timeout = 15
        t = 0
        order_number = ""
        while order_number == "" and t <= timeout:
            success_order_information_element = self.find_element(OrderPageLocators.SUCCESS_ORDER_INFORMATION_LOCATOR)
            s = success_order_information_element.text
            start_string = ': '
            end_string = '.'
            order_number = s[s.find(start_string) + len(start_string):s.rfind(end_string)]
            if order_number != "":
                print(f'Заказ создан успешно: {order_number}')
                break
            else:
                t += 0.2
                time.sleep(0.2)

        assert order_number != "", "Не удалось получить номер созданного заказа"
        return order_number

    def click_yandex_logo(self):
        tab_len = len(self.driver.window_handles)
        self.find_element(OrderPageLocators.YANDEX_LOGO_LOCATOR).click()
        assert len(self.driver.window_handles) == tab_len + 1, "Новая вкладка не открылась по клику на логотип яндекс"

    def click_samokat_logo(self):
        self.find_element(OrderPageLocators.SAMOKAT_LOGO_LOCATOR).click()
        self.wait.until(EC.url_to_be(URLs.MAIN_URL))
        assert self.driver.current_url == URLs.MAIN_URL, "По клику на Самокат-лого не произошел переход на главную страницу сервиса"
