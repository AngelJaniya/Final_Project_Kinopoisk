import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api.kinopoisk_api import FilmSeriesApi
from configuration.config_provider import ConfigProvider


@pytest.fixture
def browser():
    config = ConfigProvider()

    timeout = config.config.get("ui", {}).get("timeout", 10)

    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        driver.implicitly_wait(timeout)
        driver.maximize_window()

    yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def api_client() -> FilmSeriesApi:
    config = ConfigProvider()
    url = config.get_api_url()
    return FilmSeriesApi(url)
