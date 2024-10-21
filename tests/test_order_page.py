import pytest
import allure
from pages.order_page import OrderPage
from data import WebsiteUrls, MessageText, CorrectDataforOrder
from pages.main_page import MainPage


class TestOrderPageScooter:

    @allure.title('Проверка перехода в форму заполнения заказа через кнопку в header')
    @allure.description('Переходим по кнопке оформления заказа в блоке header, проверяем, что открылась страница с оформлением заказа')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-1')
    @allure.issue('Ссылка на баг', 'BUG-1')
    def test_transition_through_header_button_to_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.transition_to_order_through_header(driver)
        assert driver.current_url == f"{WebsiteUrls.url_order_page}"


    @allure.title('Проверка перехода в форму заполнения заказа через кнопку в блоке main')
    @allure.description('Переходим по оформления кнопке заказа в блоке main, проверяем, что открылась страница с оформлением заказа')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-2')
    @allure.issue('Ссылка на баг', 'BUG-2')
    def test_transition_through_main_div_button_to_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.transition_to_order_through_main_div(driver)
        assert driver.current_url == f"{WebsiteUrls.url_order_page}"


    @allure.title('Проверка заполнения формы с валидными значениями и создание страницы с номером заказа при переходе через кнопку заказа в header')
    @allure.description('Переходим по кнопке оформления заказа в header, заполняем валидные данные и подтверждаем оформление заказа, затем проверяем что произошел переход на страницу статуса заказа')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-3')
    @allure.issue('Ссылка на баг', 'BUG-3')
    @pytest.mark.parametrize('name, lastname, address, metro, '
                             'telephone, time_order, rental_period, color, commentary', [(CorrectDataforOrder.name_1,
                                                                           CorrectDataforOrder.lastname_1,
                                                                           CorrectDataforOrder.address_1,
                                                                           CorrectDataforOrder.metro_1,
                                                                           CorrectDataforOrder.telephone_1,
                                                                           CorrectDataforOrder.time_order_1,
                                                                           CorrectDataforOrder.rental_period_1,
                                                                           CorrectDataforOrder.color_1,
                                                                           CorrectDataforOrder.commentary_1),

                                                                          (CorrectDataforOrder.name_2,
                                                                           CorrectDataforOrder.lastname_2,
                                                                           CorrectDataforOrder.address_2,
                                                                           CorrectDataforOrder.metro_2,
                                                                           CorrectDataforOrder.telephone_2,
                                                                           CorrectDataforOrder.time_order_2,
                                                                           CorrectDataforOrder.rental_period_2,
                                                                           CorrectDataforOrder.color_2,
                                                                           CorrectDataforOrder.commentary_2)]
                             )
    def test_fill_the_form_correct_data_through_header_button(self, driver, name, lastname, address,
                                          metro, telephone, time_order, rental_period, color, commentary):
        order_page = OrderPage(driver)
        self.test_transition_through_header_button_to_order_page(driver)
        order_page.fill_the_form_for_order_scooter(name, lastname, address, metro, telephone, time_order, rental_period, color, commentary)
        final_number = order_page.get_number_of_order()
        assert driver.current_url == f"{WebsiteUrls.url_status_order_page}{final_number}"


    @allure.title('Проверка заполнения формы с валидными значениями и создание страницы с номером заказа при переходе через кнопку заказа в main')
    @allure.description('Переходим по кнопке оформления заказа в main, заполняем валидные данные и подтверждаем оформление заказа, затем проверяем что произошел переход на страницу статуса заказа')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-4')
    @allure.issue('Ссылка на баг', 'BUG-4')
    @pytest.mark.parametrize('name, lastname, address, metro, '
                             'telephone, time_order, rental_period, color, commentary', [(CorrectDataforOrder.name_1,
                                                                           CorrectDataforOrder.lastname_1,
                                                                           CorrectDataforOrder.address_1,
                                                                           CorrectDataforOrder.metro_1,
                                                                           CorrectDataforOrder.telephone_1,
                                                                           CorrectDataforOrder.time_order_1,
                                                                           CorrectDataforOrder.rental_period_1,
                                                                           CorrectDataforOrder.color_1,
                                                                           CorrectDataforOrder.commentary_1),

                                                                          (CorrectDataforOrder.name_2,
                                                                           CorrectDataforOrder.lastname_2,
                                                                           CorrectDataforOrder.address_2,
                                                                           CorrectDataforOrder.metro_2,
                                                                           CorrectDataforOrder.telephone_2,
                                                                           CorrectDataforOrder.time_order_2,
                                                                           CorrectDataforOrder.rental_period_2,
                                                                           CorrectDataforOrder.color_2,
                                                                           CorrectDataforOrder.commentary_2)]
                             )
    def test_fill_the_form_correct_data_through_main_button(self, driver, name, lastname, address,
                                          metro, telephone, time_order, rental_period, color, commentary):
        order_page = OrderPage(driver)
        self.test_transition_through_main_div_button_to_order_page(driver)
        order_page.fill_the_form_for_order_scooter(name, lastname, address, metro, telephone,
                                                                   time_order, rental_period, color, commentary)
        final_number = order_page.get_number_of_order()
        assert driver.current_url == f"{WebsiteUrls.url_status_order_page}{final_number}"



    @allure.title('Проверяем, что при успешном заказе появляется всплывающее окно с сообщением об успешном создании заказа.')
    @allure.description('Заполняем форму на оформление заказа и проверяем, что появилось всплывающее окно с текстом об успешном оформлении заказа')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-5')
    @allure.issue('Ссылка на баг', 'BUG-5')
    @pytest.mark.parametrize('name, lastname, address, metro, '
                             'telephone, time_order, rental_period, color, commentary', [(CorrectDataforOrder.name_1,
                                                                                          CorrectDataforOrder.lastname_1,
                                                                                          CorrectDataforOrder.address_1,
                                                                                          CorrectDataforOrder.metro_1,
                                                                                          CorrectDataforOrder.telephone_1,
                                                                                          CorrectDataforOrder.time_order_1,
                                                                                          CorrectDataforOrder.rental_period_1,
                                                                                          CorrectDataforOrder.color_1,
                                                                                          CorrectDataforOrder.commentary_1),

                                                                                         (CorrectDataforOrder.name_2,
                                                                                          CorrectDataforOrder.lastname_2,
                                                                                          CorrectDataforOrder.address_2,
                                                                                          CorrectDataforOrder.metro_2,
                                                                                          CorrectDataforOrder.telephone_2,
                                                                                          CorrectDataforOrder.time_order_2,
                                                                                          CorrectDataforOrder.rental_period_2,
                                                                                          CorrectDataforOrder.color_2,
                                                                                          CorrectDataforOrder.commentary_2)]
                             )
    def test_check_message_about_successful_order_with_correct_data(self, driver, name, lastname, address,
                                          metro, telephone, time_order, rental_period, color, commentary):
        order_page = OrderPage(driver)
        self.test_transition_through_main_div_button_to_order_page(driver)
        order_page.fill_the_form_for_order_scooter(name, lastname, address, metro, telephone,
                                                   time_order, rental_period, color, commentary)
        text_message = order_page.check_appearance_the_message_about_successful_order()
        assert MessageText.message_about_success_order in text_message


    @allure.title('Проверяем, что при клику по логотипу Самоката происходит на главную страницу')
    @allure.description('При тапе по логотипу Самоката происходит переход на главную страницу')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-6')
    @allure.issue('Ссылка на баг', 'BUG-6')
    def test_fill_the_form_and_transition_to_logotype_scooter(self, driver):
        order_page = OrderPage(driver)
        self.test_transition_through_main_div_button_to_order_page(driver)
        order_page.transition_to_main_page_through_logotype_scooter()
        assert driver.current_url == WebsiteUrls.url_main_page


    @allure.title('Проверяем, что при клику по логотипу Яндекса происходит на страницу Яндекс Дзена')
    @allure.description('При тапе по логотипу Яндекса происходит переход на страницу Яндекс Дзена')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-7')
    @allure.issue('Ссылка на баг', 'BUG-7')
    def test_fill_the_form_and_transition_to_logotype_yandex(self, driver):
        order_page = OrderPage(driver)
        self.test_transition_through_main_div_button_to_order_page(driver)
        order_page.transition_to_main_page_through_logotype_yandex(driver)
        assert driver.current_url == WebsiteUrls.url_yandex_dzen_page

    @allure.title('Проверка полного флоу при заказе самоката через кнопку в header, и затем после оформления, проверяем переход на страницу Яндекс Дзена через логотип')
    @allure.description('Заполняем форму на оформление заказа и проверяем, что после перехода на страницу оформленного заказа, при тапе по логотипу Яндекса происходит переход на страницу Яндекс Дзена')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-8')
    @allure.issue('Ссылка на баг', 'BUG-8')
    @pytest.mark.parametrize('name, lastname, address, metro, '
                             'telephone, time_order, rental_period, color, commentary', [(CorrectDataforOrder.name_1,
                                                                                          CorrectDataforOrder.lastname_1,
                                                                                          CorrectDataforOrder.address_1,
                                                                                          CorrectDataforOrder.metro_1,
                                                                                          CorrectDataforOrder.telephone_1,
                                                                                          CorrectDataforOrder.time_order_1,
                                                                                          CorrectDataforOrder.rental_period_1,
                                                                                          CorrectDataforOrder.color_1,
                                                                                          CorrectDataforOrder.commentary_1),

                                                                                         (CorrectDataforOrder.name_2,
                                                                                          CorrectDataforOrder.lastname_2,
                                                                                          CorrectDataforOrder.address_2,
                                                                                          CorrectDataforOrder.metro_2,
                                                                                          CorrectDataforOrder.telephone_2,
                                                                                          CorrectDataforOrder.time_order_2,
                                                                                          CorrectDataforOrder.rental_period_2,
                                                                                          CorrectDataforOrder.color_2,
                                                                                          CorrectDataforOrder.commentary_2)]
                             )
    def test_successful_order_through_header_button_to_yandex_page(self, driver, name, lastname, address,
                                          metro, telephone, time_order, rental_period, color, commentary):
        order_page = OrderPage(driver)
        self.test_transition_through_header_button_to_order_page(driver)
        order_page.fill_the_form_for_order_scooter(name, lastname, address, metro, telephone, time_order, rental_period,
                                                   color, commentary)
        order_page.confirm_the_first_page_of_form_and_make_order()
        order_page.transition_to_main_page_through_logotype_yandex(driver)
        assert driver.current_url == WebsiteUrls.url_yandex_dzen_page


    @allure.title('Проверка полного флоу при заказе самоката через кнопку в main, и затем после оформления, проверяем переход на главную страницу Самоката через логотип')
    @allure.description('Заполняем форму на оформление заказа и проверяем, что после перехода на страницу оформленного заказа, при тапе по логотипу Самоката происходит переход на страницу сайта заказа Самокатов')
    @allure.testcase('Ссылка на тест-кейс', 'TestCase-9')
    @allure.issue('Ссылка на баг', 'BUG-9')
    @pytest.mark.parametrize('name, lastname, address, metro, '
                             'telephone, time_order, rental_period, color, commentary', [(CorrectDataforOrder.name_1,
                                                                                          CorrectDataforOrder.lastname_1,
                                                                                          CorrectDataforOrder.address_1,
                                                                                          CorrectDataforOrder.metro_1,
                                                                                          CorrectDataforOrder.telephone_1,
                                                                                          CorrectDataforOrder.time_order_1,
                                                                                          CorrectDataforOrder.rental_period_1,
                                                                                          CorrectDataforOrder.color_1,
                                                                                          CorrectDataforOrder.commentary_1),

                                                                                         (CorrectDataforOrder.name_2,
                                                                                          CorrectDataforOrder.lastname_2,
                                                                                          CorrectDataforOrder.address_2,
                                                                                          CorrectDataforOrder.metro_2,
                                                                                          CorrectDataforOrder.telephone_2,
                                                                                          CorrectDataforOrder.time_order_2,
                                                                                          CorrectDataforOrder.rental_period_2,
                                                                                          CorrectDataforOrder.color_2,
                                                                                          CorrectDataforOrder.commentary_2)]
                             )
    def test_successful_order_through_header_button_to_main_scooter_page(self, driver, name, lastname, address,
                                          metro, telephone, time_order, rental_period, color, commentary):
        order_page = OrderPage(driver)
        self.test_transition_through_main_div_button_to_order_page(driver)
        order_page.fill_the_form_for_order_scooter(name, lastname, address, metro, telephone, time_order, rental_period,
                                        color, commentary)
        order_page.confirm_the_first_page_of_form_and_make_order()
        order_page.transition_to_main_page_through_logotype_yandex(driver)
        assert driver.current_url == WebsiteUrls.url_yandex_dzen_page

