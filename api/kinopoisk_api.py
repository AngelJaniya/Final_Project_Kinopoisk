import requests
from typing import Dict, Any, Tuple
import json
import os


root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

json_path = os.path.join(root_dir, 'test_data.json')

config = {}
try:
    with open(json_path, "r", encoding='utf-8') as config_file:
        config = json.load(config_file)
except Exception:

    alt_path = os.path.join(root_dir, 'test_data', 'test_data.json')
    try:
        with open(alt_path, "r", encoding='utf-8') as config_file:
            config = json.load(config_file)
    except Exception:
        config = {}

base_url_api = config.get("base_url_api")
token_info = config.get("my_headers")


class FilmSeriesApi:
    def __init__(self, url=None):

        self.url = url or base_url_api or "https://api.poiskkino.dev/v1.4/"

    def search_film_by_name(self, name: str) -> Tuple[Dict[str, Any], int]:
        api_url = f"{self.url.rstrip('/')}/movie/search"
        response = requests.get(
            api_url,
            params={"query": name},
            headers=token_info
        )
        try:
            return response.json(), response.status_code
        except Exception:
            return {}, response.status_code

    def get_movie_info(self, movie_id: int) -> Tuple[Dict[str, Any], int]:
        api_url = f"{self.url.rstrip('/')}/movie/{movie_id}"
        response = requests.get(api_url, headers=token_info)
        try:
            return response.json(), response.status_code
        except Exception:
            return {}, response.status_code

    def get_person_info(self, person_id: int) -> Tuple[Dict[str, Any], int]:
        api_url = f"{self.url.rstrip('/')}/person/{person_id}"
        response = requests.get(api_url, headers=token_info)
        try:
            return response.json(), response.status_code
        except Exception:
            return {}, response.status_code

    def search_with_invalid_params(self, params: dict) -> int:
        api_url = f"{self.url.rstrip('/')}/movie/search"
        response = requests.get(api_url, params=params, headers=token_info)
        return response.status_code

    def search_without_token(self, name: str) -> int:
        api_url = f"{self.url.rstrip('/')}/movie/search"
        response = requests.get(api_url, params={"query": name})
        return response.status_code
