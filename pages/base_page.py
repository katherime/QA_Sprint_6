from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(
                locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, driver, locator):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scrolling_to_element(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except TimeoutException:
            print(f"Element with locator {locator} not found.")

    def get_formating_locators(self, locator_1, number):
        method, locator = locator_1
        locator = locator.format(number)
        return method, locator
