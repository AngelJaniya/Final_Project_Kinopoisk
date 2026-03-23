import allure
import pytest
from api.kinopoisk_api import FilmSeriesApi


@allure.feature("API тесты Кинопоиска")
class TestKinopoiskApi:

    @allure.story("Позитивные проверки: Поиск фильмов")
    @pytest.mark.parametrize("title", [
        "Ведьмак",
        "Witcher",
        "127 часов"
    ])
    def test_search_films_positive(self, api_client: FilmSeriesApi, title):
        """Тест проверяет поиск фильма по названию"""
        body, status_code = api_client.search_film_by_name(title)

        with allure.step(f"Статус код 200 для '{title}'"):
            assert status_code == 200

        with allure.step("Проверить, что результаты найдены"):
            # Перенос строки, чтобы она не была слишком длинной
            assert len(body.get("docs", [])) > 0

        with allure.step("Проверить название первого фильма"):
            found_name = (
                body["docs"][0].get("name") or
                body["docs"][0].get("alternativeName")
            )
            assert title.lower() in found_name.lower()

    @allure.story("Негативные проверки: Безопасность")
    @pytest.mark.parametrize("title", ["Ведьмак", "Witcher", "127 часов"])
    def test_request_without_token_negative(self, api_client, title):
        """Проверка запроса без токена"""
        status_code = api_client.search_without_token(title)

        with allure.step(f"Ожидаем ошибку 401 для '{title}'"):
            assert status_code == 401
