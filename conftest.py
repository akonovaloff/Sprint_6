from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
import allure
import pytest


@pytest.fixture()
@allure.title("Работа c браузером")
def driver():
    """Фикстура для запуска и завершения работы браузера"""
    browser = "f"
    with allure.step("Открываем окно"):
        # chrome
        if "c" in browser.lower():
            driver = webdriver.Chrome()

        # yandex
        elif "y" in browser.lower():
            driver = webdriver.Chrome(service=chrome_service('C:\\Users\\Admin\\AppData\\Local'
                                                                              '\\WebDriver\\bin\\yandexdriver.exe'))

        #firefox
        elif "f" in browser.lower():
            driver = webdriver.Firefox()

        driver.maximize_window()
        yield driver

    with allure.step("Закрываем окно"):
        driver.quit()
