from selenium.webdriver.common.by import By


class MainPageLocators:
    # Header
    # Кликабельный логотип "Яндекс"
    HEADER_LOGOTYPE_YANDEX = By.XPATH, "//button[@class='Header_LogoYandex__3TSOI']"
    # Кликабельный логотип "Самокат"
    HEADER_LOGOTYPE_SCOOTER = By.XPATH, "//button[@class='Header_LogoScooter__3lsAR']"
    # Кнопка заказа самоката в header
    HEADER_BUTTON_ORDER_SCOOTER = By.XPATH, "//button[@class='Button_Button__ra12g']"
    # Кнопка проверки статуса заказа
    HEADER_BUTTON_STATUS_ORDER = By.XPATH, "//button[contains(text(),'Статус заказа')]"
    INPUT_STATUS_ORDER = By.XPATH, "//input[@placeholder='Введите номер заказа']"

    # Main
    # Кнопка заказа самоката в main
    MAIN_BUTTON_ORDER_SCOOTER = By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM"
    # Div "Вопросы о важном"
    # Общий локатор блока с вопросами
    QUESTION_LOCATOR = By.XPATH, "(//div[@id='accordion__heading-{}'])"
    # Общий локатор блока с ответами
    ANSWER_LOCATOR = By.XPATH, "(//div[@id='accordion__panel-{}'])"
    # Локатор последнего блока с вопросами
    LAST_QUESTION_LOCATOR = By.XPATH, "(//div[@id='accordion__heading-7'])[1]"
    # Локатор последнего блока с вопросами
    BUTTON_COOKIE_LOCATOR = By.XPATH, "(//button[@id='rcc-confirm-button'])"
