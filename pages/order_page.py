from selenium.webdriver.ie.webdriver import WebDriver
from helpers.locators import OrderPageLocators
from helpers.urls import URLs
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time


class OrderPage(OrderPageLocators):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.open_order_page()

    def set_name(self, name: str):
        name_field_locator = self.NAME_FIELD_LOCATOR
        name_field_element = self.driver.find_element(*name_field_locator)
        name_field_element.send_keys(name)

    def set_surname(self, surname: str):
        surname_field_locator = self.SURNAME_FIELD_LOCATOR
        surname_field_element = self.driver.find_element(*surname_field_locator)
        surname_field_element.send_keys(surname)

    def set_address(self, address: str):
        address_field_locator = self.ADDRESS_FIELD_LOCATOR
        address_field_element = self.driver.find_element(*address_field_locator)
        address_field_element.send_keys(address)

    def set_phone(self, phone: str):
        phone_field_locator = self.PHONE_FIELD_LOCATOR
        phone_field_element = self.driver.find_element(*phone_field_locator)
        phone_field_element.send_keys(phone)

    def click_confirm_button(self):
        buttons = self.driver.find_elements(*self.CONFIRM_BUTTON)
        if len(buttons) == 1:
            index = 0
        elif len(buttons) == 2:
            index = 1
        else:
            index = -1
        buttons[index].click()

        wait(self.driver, 3).until(
            EC.visibility_of_element_located(self.DELIVERY_DATE_FIELD_LOCATOR) or
            EC.visibility_of_element_located(self.ORDER_ERROR_MESSAGE_LOCATOR) or
            EC.visibility_of_element_located(self.ORDER_CONFIRMATION_FORM_LOCATOR) or
            EC.visibility_of_element_located(self.SUCCESS_ORDER_INFORMATION_LOCATOR))

    def select_random_metro_station(self):
        self.driver.find_element(*self.METRO_FIELD_LOCATOR).click()
        wait(self.driver, 3).until(EC.visibility_of_element_located(self.METRO_STATION_SELECTOR_LOCATOR))
        metro_station_list = self.driver.find_elements(*self.METRO_STATION_SELECTOR_LOCATOR)
        n = randint(0, len(metro_station_list) - 1)
        print(f"Выбрана станция метро: {metro_station_list[n].text}")
        self.driver.execute_script("arguments[0].scrollIntoView();", metro_station_list[n])
        metro_station_list[n].click()

    def set_delivery_date(self):
        self.driver.find_element(*self.DELIVERY_DATE_FIELD_LOCATOR).click()
        wait(self.driver, 1).until(EC.visibility_of_element_located(self.TODAY_CALENDAR_LOCATOR))
        self.driver.find_element(*self.TODAY_CALENDAR_LOCATOR).click()

    def set_random_rental_period(self):
        self.driver.find_element(*self.RENTAL_PERIOD_FIELD_LOCATOR).click()
        wait(self.driver, 3).until(EC.visibility_of_element_located(self.RENTAL_PERIOD_DROPDOWN_MENU_LOCATOR))
        rental_options_elements = self.driver.find_elements(*self.RENTAL_PERIOD_OPTIONS_LOCATOR)
        n = randint(0, len(rental_options_elements) - 1)
        rental_options_elements[n].click()

    def set_random_color_option(self):
        color_option_elements = self.driver.find_elements(*self.COLOR_OPTIONS_LOCATOR)
        color_len = len(color_option_elements)
        n = randint(0, color_len - 1)
        color_option_elements[n].click()

    def get_order_number(self):
        timeout = 15
        t = 0
        order_number = ""
        while order_number == "" and t <= timeout:
            success_order_information_element = self.driver.find_element(*self.SUCCESS_ORDER_INFORMATION_LOCATOR)
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
        self.driver.find_element(*self.YANDEX_LOGO_LOCATOR).click()
        assert len(self.driver.window_handles) == tab_len + 1, "Новая вкладка не открылась по клику на логотип яндекс"

    def click_samokat_logo(self):
        self.driver.find_element(*self.SAMOKAT_LOGO_LOCATOR).click()
        wait(self.driver, 3).until(EC.url_to_be(URLs.MAIN_URL))
        assert self.driver.current_url == URLs.MAIN_URL, "По клику на Самокат-лого не произошел переход на главную страницу сервиса"


    def open_order_page(self):
        self.driver.get(URLs.ORDER_URL)
        wait(self.driver, 3).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
