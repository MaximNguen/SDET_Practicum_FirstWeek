from selenium.webdriver.remote.webdriver import WebDriver
import allure


class PageFactory:
    """
    Фабрика для создания и управления страницами.
    Реализует паттерн Factory.
    """
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page = None
    
    def get_main_page(self, refresh: bool = False) -> object:
        """Получить экземпляр страницы."""
        if refresh or self.page is None:
            with allure.step("Создаем экземпляр главной страницы"):
                from pages.main_page import MainPage
                self.page = MainPage(self.driver)
        
        return self.page
    
    def reset(self):
        """Сбросить состояние страницы (очистить кэш)."""
        with allure.step("Сбрасываем состояние страницы"):
            self.page = None