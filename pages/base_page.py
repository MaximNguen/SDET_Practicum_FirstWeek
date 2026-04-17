from selenium.webdriver.remote.webelement import WebElement
from typing import List

from utils.waitHelpers import WaitHelpers as WH

class BasePage:
    """
    Базовая страница для всех страниц приложения.
    Содержит общие методы для взаимодействия
    с элементами страницы.
    """
    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver
        self.wait = WH(self.driver)
        
    def find_element(self, *locator) -> WebElement:
        """Поиск элемента на странице по локатору."""
        return self.driver.find_element(*locator)
    
    def click(self, *locator) -> None:
        """Клик по элементу, найденному по локатору."""
        self.wait.wait_for_clickable(locator)
        self.find_element(*locator).click()
        
    def find_elements(self, *locator) -> List[WebElement]:
        """Поиск всех элементов на странице по локатору."""
        return self.driver.find_elements(*locator)