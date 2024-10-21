import pytest
import allure
from data import TextAnswers, WebsiteUrls
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title('Проверка списка ответов и вопросов в блоке «Вопросы о важном»')
    @allure.description('Прокликиваем каждый блок вопросов и сравниваем соответствие текста в блоке ответов')
    @pytest.mark.parametrize('number, expected_result', [(0, TextAnswers.answer_0), (1, TextAnswers.answer_1),
                                                         (2, TextAnswers.answer_2), (3, TextAnswers.answer_3),
                                                         (4, TextAnswers.answer_4), (5, TextAnswers.answer_5),
                                                         (6, TextAnswers.answer_6), (7, TextAnswers.answer_7)])
    def test_display_and_text_questions_and_answers(self, driver, number, expected_result):
        main_page = MainPage(driver)
        driver.get(WebsiteUrls.url_main_page)
        main_page.click_to_element(driver, MainPageLocators.BUTTON_COOKIE_LOCATOR)
        assert main_page.get_div_answers_text(driver, number) == expected_result
