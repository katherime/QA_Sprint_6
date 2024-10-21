import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import WebsiteUrls



class MainPage(BasePage):

    @allure.step('Возвращение текст ответа на вопрос при клике по блоку вопросов в "Вопросы о важном"')
    def get_div_answers_text(self, driver, number):
        locator_question_formatted = self.get_formating_locators(
            MainPageLocators.QUESTION_LOCATOR, number)
        locator_answer_formatted = self.get_formating_locators(
            MainPageLocators.ANSWER_LOCATOR, number)
        self.scrolling_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.click_to_element(driver, locator_question_formatted)
        return self.get_text_from_element(locator_answer_formatted)

    @allure.step('Переход на страницу заказа через кнопку в header страницы')
    def transition_to_order_through_header(self, driver):
        driver.get(WebsiteUrls.url_main_page)
        self.find_element_with_wait(MainPageLocators.BUTTON_COOKIE_LOCATOR)
        self.click_to_element(self.driver, MainPageLocators.BUTTON_COOKIE_LOCATOR)
        self.click_to_element(self.driver, MainPageLocators.HEADER_BUTTON_ORDER_SCOOTER)
        self.find_element_with_wait(OrderPageLocators.INPUT_NAME)

    @allure.step('Переход на страницу заказа через кнопку в центре страницы')
    def transition_to_order_through_main_div(self, driver):
        driver.get(WebsiteUrls.url_main_page)
        self.click_to_element(self.driver, MainPageLocators.BUTTON_COOKIE_LOCATOR)
        self.scrolling_to_element(MainPageLocators.MAIN_BUTTON_ORDER_SCOOTER)
        self.click_to_element(self.driver, MainPageLocators.MAIN_BUTTON_ORDER_SCOOTER)
        self.find_element_with_wait(OrderPageLocators.INPUT_NAME)

