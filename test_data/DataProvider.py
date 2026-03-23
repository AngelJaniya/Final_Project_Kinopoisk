import json
import os

current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, 'test_data.json')

try:
    with open(json_path, encoding='utf-8') as my_file:
        global_data = json.load(my_file)
except FileNotFoundError:
    global_data = {}


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop: str) -> str:
        return self.data.get(prop)

    def get_headers(self) -> dict:
        return self.data.get("my_headers", {})
