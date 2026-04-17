from selenium.webdriver.common.by import By

class MainPageLocators:
    """Класс для хранения локаторов элементов и значений ячеек на странице."""
    
    navbar_list = (By.CSS_SELECTOR, 'ul.nav-pills.categorymenu')
    search_input = (By.ID, 'filter_keyword')
    cart_button = (By.LINK_TEXT, 'Cart')