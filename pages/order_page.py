import re
import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import CorrectDataforOrder


class OrderPage(BasePage):

    @allure.step('Заполняем поле введения имени')
    def fill_the_form_input_name(self, name):
        self.add_text_to_element(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Заполняем поле введения фамилии')
    def fill_the_form_input_lastname(self, lastname):
        self.add_text_to_element(OrderPageLocators.INPUT_LASTNAME, lastname)

    @allure.step('Заполняем поле введения адреса')
    def fill_the_form_input_address(self, address):
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Заполняем поле введения метро')
    def fill_the_form_input_metro(self, metro):
        self.click_to_element(self.driver, OrderPageLocators.INPUT_METRO)
        self.click_to_element(self.driver, metro)

    @allure.step('Заполняем поле введения номера телефона')
    def fill_the_form_input_telephone(self, telephone):
        self.add_text_to_element(OrderPageLocators.INPUT_NUMBER, telephone)

    @allure.step('Подтвеждаем через кнопку "Далее" заполнение первой страницы оформления заказа')
    def confirm_the_first_page_of_form(self):
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_NEXT)
        self.find_element_with_wait(OrderPageLocators.INPUT_DELIVERY)

    @allure.step('Заполняем поле введения даты доставки самоката')
    def fill_the_form_input_time_delivery(self, time_order):
        self.add_text_to_element(OrderPageLocators.INPUT_DELIVERY, time_order)

    @allure.step('Выбираем цвет в блоке выбора цвета самоката')
    def fill_the_form_input_color(self, color):
        self.click_to_element(self.driver, color)

    @allure.step('Заполняем поле введения времени доставки')
    def fill_the_form_input_rental_period(self, rental_period):
        self.click_to_element(self.driver, OrderPageLocators.INPUT_RENTAL_PERIOD)
        self.click_to_element(self.driver, rental_period)

    @allure.step('Заполняем поле введения комментария')
    def fill_the_form_input_commentary(self, commentary):
        self.add_text_to_element(OrderPageLocators.INPUT_COMMENTARY, commentary)

    @allure.step('Подтверждаем через кнопку "Заказать" заполнение второй страницы оформления заказа')
    def confirm_the_first_page_of_form_and_make_order(self):
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_CHECK_STATUS)

    def fill_the_form_for_order_scooter(self, name, lastname, address, metro, telephone, time_order, rental_period,
                                        color, commentary):
        self.fill_the_form_input_name(name)
        self.fill_the_form_input_lastname(lastname)
        self.fill_the_form_input_address(address)
        self.fill_the_form_input_metro(metro)
        self.fill_the_form_input_telephone(telephone)
        self.confirm_the_first_page_of_form()
        self.fill_the_form_input_time_delivery(time_order)
        self.fill_the_form_input_color(color)
        self.fill_the_form_input_rental_period(rental_period)
        self.fill_the_form_input_commentary(commentary)
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_MAKE_ORDER)
        self.find_element_with_wait(OrderPageLocators.BUTTON_CONFIRM_ORDER)
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_CONFIRM_ORDER)

    @allure.step('Заполнение формы с дефолтными валидными значениями')
    def fill_the_form_for_order_scooter_default_data(self):
        self.fill_the_form_input_name(CorrectDataforOrder.name_1)
        self.fill_the_form_input_lastname(CorrectDataforOrder.lastname_1)
        self.fill_the_form_input_address(CorrectDataforOrder.address_1)
        self.fill_the_form_input_metro(CorrectDataforOrder.metro_1)
        self.fill_the_form_input_telephone(CorrectDataforOrder.telephone_1)
        self.confirm_the_first_page_of_form()
        self.fill_the_form_input_time_delivery(CorrectDataforOrder.time_order_1)
        self.fill_the_form_input_color(CorrectDataforOrder.color_1)
        self.fill_the_form_input_rental_period(CorrectDataforOrder.rental_period_1)
        self.fill_the_form_input_commentary(CorrectDataforOrder.commentary_1)
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_MAKE_ORDER)
        self.find_element_with_wait(OrderPageLocators.BUTTON_CONFIRM_ORDER)
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_CONFIRM_ORDER)
        successful_text = self.get_text_from_element(OrderPageLocators.DIV_SUCCESSFUL_ORDER)
        return successful_text

    @allure.step('Получение номера оформленного заказа после заполнения анкеты')
    def get_number_of_order(self):
        number_text = self.get_text_from_element(OrderPageLocators.NUMBER_OF_ORDER_LOCATOR)
        final_number = ''.join(re.findall(r'\d', number_text))
        self.click_to_element(self.driver, OrderPageLocators.BUTTON_CHECK_STATUS)
        self.find_element_with_wait(OrderPageLocators.BUTTON_LOOK_STATUS)
        return final_number

    @allure.step('Клик по логотипу Самокат в header')
    def transition_to_main_page_through_logotype_scooter(self):
        self.click_to_element(self.driver, OrderPageLocators.LOGOTYPE_SCOOTER)
        self.find_element_with_wait(MainPageLocators.HEADER_BUTTON_ORDER_SCOOTER)

    @allure.step('Клик по логотипу Яндекса в header')
    def transition_to_main_page_through_logotype_yandex(self, driver):
        self.click_to_element(self.driver, OrderPageLocators.LOGOTYPE_YANDEX)
        driver.switch_to.window(driver.window_handles[-1])
        self.find_element_with_wait(OrderPageLocators.SEARCH_INPUT_YANDEX)

    @allure.step('Получение текста из сплывающего окна после оформления заказа')
    def check_appearance_the_message_about_successful_order(self):
        successful_text = self.get_text_from_element(OrderPageLocators.NUMBER_OF_ORDER_LOCATOR)
        return successful_text
