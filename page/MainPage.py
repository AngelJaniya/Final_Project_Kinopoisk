import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.config_provider import ConfigProvider


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.config = ConfigProvider()
        # Получаем базовый URL из конфига
        base_url = self.config.get_ui_url()
        self.__driver.get(base_url)

    @allure.step("Поиск фильма: {title}")
    def search(self, title: str) -> None:
        """
        Метод вводит любое название: 'Ведьмак', ' Witcher' или '127 часов'.
        """
        # Ждем, пока поле поиска станет доступным
        search_input = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[name='kp_query']"))
        )
        search_input.clear()
        search_input.send_keys(title, Keys.RETURN)

    @allure.step("Получить название текущей вкладки")
    def get_title_tab(self) -> str:
        """Возвращает заголовок страницы для проверки в тесте"""
        return self.__driver.title
