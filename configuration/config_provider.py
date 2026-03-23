import json
import os


class ConfigProvider:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self.json_path = os.path.join(
            current_dir, '..', 'test_data', 'test_data.json')

        try:
            with open(self.json_path, "r", encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    def get_api_url(self) -> str:
        return self.config.get("base_url_api")

    def get_token(self) -> dict:
        return self.config.get("my_headers")
