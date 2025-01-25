import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.locators import AccordionLocators, MainPageLocators
from helpers.urls import URLs
from conftest import driver
import allure
import time


class TestAccordion(AccordionLocators, MainPageLocators):
    @allure.feature("Вопросы о важном")
    @allure.title("Проверяем секцию «Вопросы о важном»")
    @allure.description(
        "Тест проверяет, что на главной странице присутствуют все вопросы из списка, и что ответы на них отображаются "
        "по клику")
    @pytest.mark.parametrize("question_text, answer_text", [
        # 1
        ("Сколько это стоит? И как оплатить?",
         "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        # 2
        ("Хочу сразу несколько самокатов! Так можно?",
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать "
         "несколько заказов — один за другим."),
        # 3
        ("Как рассчитывается время аренды?",
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды "
         "начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, "
         "суточная аренда закончится 9 мая в 20:30."),
        # 4
        ("Можно ли заказать самокат прямо на сегодня?",
         "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        # 5
        ("Можно ли продлить заказ или вернуть самокат раньше?",
         "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        # 6
        ("Вы привозите зарядку вместе с самокатом?",
         "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без "
         "передышек и во сне. Зарядка не понадобится."),
        # 7
        ("Можно ли отменить заказ?",
         "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        # 8
        ("Я жизу за МКАДом, привезёте?",
         "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_accordion_item_success(self, driver, question_text, answer_text):
        # question_text = "Сколько это стоит? И как оплатить?"
        # answer_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        question_xpath = f"//*[contains(text(), '{question_text}')]"
        answer_xpath = f"{question_xpath}/../..//*[contains(text(), '{answer_text}')]"
        page = URLs.MAIN_URL

        with allure.step(f"Открываем страницу: {page}"):
            driver.get(page)

        with allure.step(f"Ожидание загрузки страницы"):
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(self.ACCORDION_SECTION)
            )
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(self.SCOOTER_IMG_LOCATOR)
            )
        with allure.step("Поиск элемента на странице"):
            accordion_item_element = driver.find_element(By.XPATH, question_xpath)

        with allure.step("Скролл до найденного элемента и клик"):
            driver.execute_script("arguments[0].scrollIntoView();", accordion_item_element)
            time.sleep(0.5)
            accordion_item_element.click()


        with allure.step("Поиск текста ответа на вопрос"):
            answer_element = driver.find_element(By.XPATH, answer_xpath)
            assert answer_element.text == answer_text, f"Текст ответа не совпадает с ожидаемым"

        with allure.step("Проверка видимости текста ответа на вопрос"):
            driver.execute_script("arguments[0].scrollIntoView();", answer_element)
            assert answer_element.is_displayed(), "Текст ответа найден на странице, но он не отображается"
