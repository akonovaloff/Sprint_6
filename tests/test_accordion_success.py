import pytest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from helpers.urls import URLs
from conftest import driver
import allure
import time

QA_DATA = [
    # 1
    {"question": "Сколько это стоит? И как оплатить?",
     "answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."},
    # 2
    {"question": "Хочу сразу несколько самокатов! Так можно?",
     "answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать "
               "несколько заказов — один за другим."},
    # 3
    {"question": "Как рассчитывается время аренды?",
     "answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды "
               "начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, "
               "суточная аренда закончится 9 мая в 20:30."},
    # 4
    {"question": "Можно ли заказать самокат прямо на сегодня?",
     "answer": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."},
    # 5
    {"question": "Можно ли продлить заказ или вернуть самокат раньше?",
     "answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."},
    # 6
    {"question": "Вы привозите зарядку вместе с самокатом?",
     "answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без "
               "передышек и во сне. Зарядка не понадобится."},
    # 7
    {"question": "Можно ли отменить заказ?",
     "answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."},
    # 8
    {"question": "Я жизу за МКАДом, привезёте?",
     "answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области."}
]


class TestAccordion:
    @allure.feature("Вопросы о важном")
    @allure.title("Проверяем секцию «Вопросы о важном»")
    @allure.description(
        "Тест проверяет, что на главной странице присутствуют все вопросы из списка, и что ответы на них отображаются "
        "по клику")
    @pytest.mark.parametrize("qa_data", QA_DATA)
    def test_accordion_item_success(self, driver, qa_data):
        question_text = qa_data["question"]
        answer_text = qa_data["answer"]
        question_xpath = f"//*[contains(text(), '{question_text}')]"
        answer_xpath = f"{question_xpath}/../..//p"

        page = BasePage(driver, URLs.MAIN_URL)
        question_element = page.find_element((By.XPATH, question_xpath))
        answer_element = page.find_element((By.XPATH, answer_xpath))
        page.scroll_to_element(question_element)
        assert answer_element.is_displayed() == False, "Ответ не должен отображаться до клика по вопросу"
        question_element.click()
        time.sleep(0.1)
        assert answer_element.is_displayed() == True, "Ответ должен отображаться после клика по вопросу"
        assert answer_element.text == answer_text, "Текст ответа не совпадает с ожидаемым"
