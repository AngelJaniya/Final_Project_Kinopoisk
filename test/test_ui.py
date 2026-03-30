import allure
import pytest
from api.kinopoisk_api import FilmSeriesApi


@allure.epic("Дипломный проект")
@allure.feature("API тесты Кинопоиска")
class TestKinopoiskApi:

    @allure.story("Позитивные проверки: Поиск фильмов по названию")
    @pytest.mark.parametrize("title", [
        "Ведьмак",      # Кириллица
        "Witcher",      # Латиница
        "127 часов"     # Цифры
    ])
    def test_search_films_positive(self, api_client: FilmSeriesApi, title):
        """Тест проверяет поиск фильма по названию (Статус 200)"""
        body, status_code = api_client.search_film_by_name(title)

        with allure.step(f"Проверить статус код 200 для '{title}'"):
            assert status_code == 200

        with allure.step("Проверить наличие результатов"):
            assert len(body.get("docs", [])) > 0

        with allure.step("Проверить название первого фильма"):
            found_name = (body["docs"][0].get("name") or
                          body["docs"][0].get("alternativeName"))
            assert title.lower() in found_name.lower()

    @allure.story("Негативные проверки: Безопасность (Запрос без токена)")
    @pytest.mark.parametrize("title", [
        "Ведьмак",      # Кириллица
        "Witcher",      # Латиница
        "127 часов"     # Цифры
    ])
    def test_request_without_token_negative(
            self, api_client: FilmSeriesApi, title):
        """Тест проверяет, что поиск БЕЗ токена невозможен (Статус 401)"""
        status_code = api_client.search_without_token(title)

        with allure.step(f"Ожидаем ошибку 401 для запроса '{title}'"):
            assert status_code == 401

    @allure.story("Негативные проверки: Параметры")
    @allure.title("Отправка запроса с пустым названием")
    def test_search_with_empty_title(self, api_client: FilmSeriesApi):
        """Проверка реакции API на пустую строку поиска"""
        body, status_code = api_client.search_film_by_name("")
        with allure.step("Проверить, что сервер вернул статус 200 или 400"):
            assert status_code in [200, 400]
