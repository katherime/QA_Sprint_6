from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поле ввода имени
    INPUT_NAME = By.XPATH, "//input[@placeholder='* Имя']"

    # Поле ввода фамилии
    INPUT_LASTNAME = By.XPATH, "//input[@placeholder='* Фамилия']"

    # Поле ввода адреса
    INPUT_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"

    # Поле ввода станции метро
    INPUT_METRO = By.XPATH, "//input[@placeholder='* Станция метро']"

    # Первая кнопка выбора метро
    BUTTON_FIRST_METRO = By.XPATH, "//button[@value='1']"

    # Первая кнопка выбора метро
    BUTTON_SECOND_METRO = By.XPATH, "//button[@value='2']"


    # Поле ввода телефона
    INPUT_NUMBER = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    # Кнопка для заказа "Далее"
    BUTTON_NEXT = By.XPATH, "//button[contains(text(),'Далее')]"

    # Поле ввода даты доставки самоката
    INPUT_DELIVERY = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"

    # Поле ввода срока аренды
    INPUT_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-placeholder']"
    # Первая кнопка в выборе срока аренды
    BUTTON_FIRST_VAR_RENTAL = By.XPATH, "//div[@class='Dropdown-option'][1]"
    # Вторая кнопка в выборе срока аренды
    BUTTON_SECOND_VAR_RENTAL = By.XPATH, "//div[@class='Dropdown-option'][2]"

    # Поле выбора цвета черный жемчуг
    BUTTON_CHOOSE_BLACK_COLOR = By.XPATH, "//label[contains(text(),'чёрный жемчуг')]"

    # Поле выбора цвета черный жемчуг
    BUTTON_CHOOSE_GRAY_COLOR = By.XPATH, "//label[contains(text(),'серая безысходность')]"

    # Поле ввода комментарий
    INPUT_COMMENTARY = By.XPATH, "//input[@placeholder='Комментарий для курьера']"

    # Кнопка оформления заказа
    BUTTON_MAKE_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    # Кнопка подтверждения заказа
    BUTTON_CONFIRM_ORDER = By.XPATH, "//button[contains(text(),'Да')]"

    # Локатор номера заказа
    NUMBER_OF_ORDER_LOCATOR = By.XPATH, "//div[@class='Order_Text__2broi']"

    # Кнопка просмотра статуса после создания заказа
    BUTTON_CHECK_STATUS = By.XPATH, "//button[contains(text(),'Посмотреть статус')]"

    # Сообщение об успешном оформлении заказа
    DIV_SUCCESSFUL_ORDER = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"

    # Кнопка
    BUTTON_LOOK_STATUS = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    # Логотип самокат
    LOGOTYPE_SCOOTER = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"

    # Логотип Яндекса
    LOGOTYPE_YANDEX = By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"

    # Поискова страница Яндекса при открытии новой вкладки
    SEARCH_INPUT_YANDEX = By.XPATH, "//div[@class='dzen-desktop--ya-search-micro-app__yandexSearchContainer-Ym']"
