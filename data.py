from locators.order_page_locators import OrderPageLocators
class WebsiteUrls:
    # Главная страница
    url_main_page = 'https://qa-scooter.praktikum-services.ru/'

    # Страница оформления заказа
    url_order_page = 'https://qa-scooter.praktikum-services.ru/order'

    # Страница отслеживания заказа
    url_status_order_page = 'https://qa-scooter.praktikum-services.ru/track?t='

    # Страница яндекс дзена
    url_yandex_dzen_page = "https://dzen.ru/?yredirect=true"

class MessageText:
    # Главная страница
    successful_text = 'Заказ оформлен'

    message_about_success_order = 'Номер заказа'


class TextAnswers:
    # Текста ответов на вопросы
    answer_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    answer_1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    answer_2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    answer_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    answer_4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    answer_5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    answer_6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    answer_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class CorrectDataforOrder:
    # Имя
    name_1 = 'Екатерина'
    name_2 = 'Ольга'
    # Фамилия
    lastname_1 = 'Иванова'
    lastname_2 = 'Петрова'
    # Адрес
    address_1 = 'г.Москва, улица Красная, дом 12'
    address_2 = 'г.Пермь'
    # Метро
    metro_1 = OrderPageLocators.BUTTON_FIRST_METRO
    metro_2 = OrderPageLocators.BUTTON_SECOND_METRO

    # Телефон
    telephone_1 = '+7123456789'
    telephone_2 = '+7987654321'
    # Дата для заказа
    time_order_1 = '12.12.2024'
    time_order_2 = '01.02.2027'

    # Срок аренды
    rental_period_1 = OrderPageLocators.BUTTON_FIRST_VAR_RENTAL
    rental_period_2 = OrderPageLocators.BUTTON_SECOND_VAR_RENTAL

    # Цвет
    color_1 = OrderPageLocators.BUTTON_CHOOSE_BLACK_COLOR
    color_2 = OrderPageLocators.BUTTON_CHOOSE_GRAY_COLOR
    # Комментарии
    commentary_1 = '123456789'
    commentary_2 = '-'
