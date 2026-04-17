from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitHelpers:
    """
    Класс утилитов ожидания элементов
    """
    def __init__(self, driver):
        self.driver = driver
        
    def wait_for_element(self, locator, timeout=10):
        """Метод ожидания видимости элемента"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Элемент с локатором {locator} не найден в течение {timeout} секунд.")
            return None
        
    def wait_for_clickable(self, locator, timeout=10):
        """Метод проверки кликабельности элемента"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"Элемент с локатором {locator} не кликабельный в течение {timeout} секунд.")
            return None