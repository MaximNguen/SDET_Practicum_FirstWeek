import allure
import pytest
import random

from data.urls import main_page_url
from data.expected_data import expected_categories

@allure.epic("Проверка производительности фильтра товаров")
@allure.feature("Тест-кейсы для проверки производительности фильтра товаров")
class TestFilterPerformance:
    """Тест-кейсы для проверки производительности фильтра товаров."""

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения тест-кейсов на производительность фильтра товаров ==========")

    @classmethod
    def teardown_class(cls):
        print("\n========= Конец выполнения тест-кейсов на производительность фильтра товаров ==========")

    @pytest.fixture(autouse=True)
    def setup(self, main_page, items_page, url=main_page_url):
        self.main_page = main_page
        self.items_page = items_page
        self.main_page.open(url)
        yield self.main_page
        self.main_page.quit()
        
    @allure.story("Проверка наличия товаров всех категориях и количество товаров не меньше 4")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_products_in_category(self):
        """Проверка наличия товаров в каждой категории и количество товаров не меньше 4."""
        categories = self.main_page.get_navbar_items()
        for category in categories:
            with allure.step(f"Проверяем наличие товаров в категории: {category}"):
                self.main_page.click_category(category)
                products_data = self.items_page.get_products_names()
                assert products_data, f"На странице категории '{category}' не найдено товаров."
                assert len(products_data) >= 4, f"На странице категории '{category}' найдено меньше 4 товаров."
                
    @allure.story("Проверка кликабельности сортировки товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_filter_performance(self):
        """Проверка кликабельности сортировки товаров."""
        category = random.choice(expected_categories)
        with allure.step("Переходим на страницу 1 из категорий"):
            self.main_page.click_category(category)
        with allure.step(f"Проверяем наличие сортировку товаров в категории: {category}"):
            select = self.items_page.get_filter_select()
            assert select.is_displayed(), f"Фильтр не отображается на сайте"