import os
import requests
import json
from . import constants


class Settings:
    def __init__(self):
        self.settings = None

    def get_settings_json(self, local=False):
        if constants.TEST_MODE or local:
            settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
            with open(settings_path, "r", encoding="utf-8") as f:
                self.settings = json.load(f)
        else:
            if self.settings is None:
                response = requests.get(constants.SETTINGS_URL, timeout=5)
                self.settings = response.json()
        return self.settings

    def get_version(self):
        local_settings = self.get_settings_json(local=True)
        return local_settings.get("version", "1.0.0")

    def get_repo_address(self):
        return constants.REPO_URL

    def get_bitcoin_address(self):
        settings = self.get_settings_json()
        return settings.get("bitcoin", {})

    def get_buy_me_a_coffee(self):
        settings = self.get_settings_json()
        return settings.get("buy_me_a_coffee", "")
