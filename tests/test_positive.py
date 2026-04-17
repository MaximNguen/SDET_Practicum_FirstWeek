import allure
import pytest
import random

from data.urls import main_page_url
from data.expected_data import expected_categories
from data.mock_data import random_category
from pages.main_page import MainPage

@allure.epic("UI Тесты")
@allure.feature("Позитивные тест-кейсы")
class TestPositiveResult:
    """Позитивные тест-кейсы для формы."""

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения позитивного тест-кейса ==========")

    @classmethod
    def teardown_class(cls):
        print("========= Конец выполнения позитивного тест-кейса ==========")

    @pytest.fixture(autouse=True)
    def setup(self, main_page, url=main_page_url):
        self.main_page = main_page
        self.main_page.open(url)
        yield self.main_page
        
    @allure.story("Проверка наличия категорий в навигационной панели")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navbar_categories(self):
        """Проверка наличия категорий в навигационной панели."""
        categories = self.main_page.get_navbar_items()
        name_category = [item.text.strip().upper() for item in categories]
        
        for category in expected_categories:
            with allure.step(f"Проверяем наличие категории: {category}"):
                print("Категории на странице:", name_category)
                assert category.upper() in name_category, f"Категория '{category}' не найдена в навигационной панели."
                
    @allure.story("Проверка кликабельности категорий в навигационной панели")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_category(self):
        """Проверка кликабельности категорий в навигационной панели."""
        category = random.choice(random_category)
        with allure.step(f"Проверяем кликабельность категории: {category}"):
            for item in self.main_page.get_navbar_items():
                if item.text.strip() == category and item.text.strip() != 'HOME':
                    self.main_page.click_category(category)
                    assert self.main_page.driver.current_url != main_page_url, f"Клик по категории '{category}' не привел к переходу на другую страницу."
                    
    @allure.story("Проверка кликабельности всех категорий")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_all_categories(self):
        """Проверка кликабельности каждой категории в навигационной панели."""
        categories = self.main_page.get_navbar_items_text()
        
        for category in categories:
            with allure.step(f"Кликаем и проверяем категорию: {category}"):
                self.main_page.click_category(category)
                
                current_url = self.main_page.driver.current_url
                assert current_url != main_page_url, \
                    f"Клик по категории '{category}' не привел к переходу"
                
                self.main_page.open(main_page_url)