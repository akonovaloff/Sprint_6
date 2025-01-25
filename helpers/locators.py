from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    METRO_STATION_SELECTOR_LOCATOR = (By.XPATH, "//div[@class='select-search__select']//li")
    DELIVERY_DATE_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TODAY_CALENDAR_LOCATOR = (By.XPATH, "//div[contains(@class, '__day--today')]")
    ORDER_ERROR_MESSAGE_LOCATOR = (By.XPATH, "//div[@class='Input_ErrorMessage__3HvIb Input_Visible___syz6']")
    RENTAL_PERIOD_FIELD_LOCATOR = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_DROPDOWN_MENU_LOCATOR = (By.CLASS_NAME, "Dropdown-menu")
    RENTAL_PERIOD_OPTIONS_LOCATOR = (By.XPATH, "//*[contains(@class, 'Dropdown-option')]")
    COLOR_OPTIONS_LOCATOR = (By.CLASS_NAME, "Checkbox_Input__14A2w")
    ORDER_CONFIRMATION_FORM_LOCATOR = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_ORDER_INFORMATION_LOCATOR = (By.CLASS_NAME, "Order_Text__2broi")
    YANDEX_LOGO_LOCATOR = (By.XPATH, "//img[@alt='Yandex']")
    SAMOKAT_LOGO_LOCATOR = (By.XPATH, "//img[@alt='Scooter']")


class AccordionLocators:
    ACCORDION_SECTION = (By.CLASS_NAME, 'accordion')

class MainPageLocators:
    ACCORDION_SECTION = (By.CLASS_NAME, 'accordion')
    ACCORDION_ITEMS_LOCATOR = (By.CLASS_NAME, "accordion__item")
    ACCORDION_HEADING = (By.CLASS_NAME, 'accordion__heading')
    ACCORDION_PANEL = (By.CLASS_NAME, 'accordion__panel')
    TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    SCOOTER_IMG_LOCATOR = (By.XPATH, "//img[@alt='Scooter blueprint']")
