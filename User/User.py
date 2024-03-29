from ursina import *

import Game
from Statistics import Statistics
from .UserData import UserData
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact
from Entity.Weapon.Weapon import Weapon
from typing import List
import json


class User:
    def __init__(self, username: str, is_guest: bool):
        self._username = username
        self._user_data = UserData()
        self._is_guest = is_guest
        self._gp = 0
        self._ranking = 'unranked', ''

    @property
    def username(self) -> str:
        return self._username

    @property
    def user_data(self) -> UserData:
        return self._user_data

    @property
    def gp(self) -> int:
        return self._gp

    @property
    def ranking(self) -> tuple:
        return self._ranking

    def get_equipped_character(self) -> Character:
        return self._user_data.equipped_character

    def get_money(self) -> int:
        return self._user_data.money

    def add_money(self, amount):
        self._user_data.add_money(amount)
        Game.stats.add_money(amount)

    def remove_money(self, amount):
        self._user_data.remove_money(amount)
        Game.stats.spend_money(amount)

    def get_characters(self) -> List[Character]:
        return self._user_data.characters

    def get_artifacts(self) -> List[Artifact]:
        return self._user_data.artifacts

    def get_weapons(self) -> List[Weapon]:
        return self._user_data.weapons

    def get_stats(self) -> Statistics:
        return self._user_data.statistics

    def replace_data(self, json_str):
        self._user_data = UserData(json_str)

    def add_character(self, character: Character):
        self._user_data.add_character(character)

    def add_artifact(self, artifact: Artifact):
        self._user_data.add_artifact(artifact)

    def add_weapon(self, weapon: Weapon):
        self._user_data.add_weapon(weapon)

    def equip_character(self, character: Character):
        self._user_data.equip_character(character)

    def calculate_gp(self):
        if self._user_data.data_parsed:
            data = self._user_data.jsonify_data()
        else:
            data = {
                'inventory': {
                    'characters': self._user_data.characters,
                    'artifacts': self._user_data.artifacts,
                    'weapons': self._user_data.weapons
                }
            }

        rating = Game.rating_program.rater.generate_power_details(data, True)
        self._gp = rating['rating']['weighted']
        self._ranking = rating['ranking']['tier'], rating['ranking']['tier value']

    def load(self):
        self._user_data.load_items()

    def save_data(self):
        Game.migrate_stats_to_user()
        if self._is_guest:
            json.dump(self._user_data.jsonify_data(), open(f"Data/{self._username}.json", "w"), indent=4)

    def unload(self):
        self.save_data()

        [destroy(item) for item in self._user_data.characters]
        [destroy(item) for item in self._user_data.weapons]

    def __repr__(self):
        print(self._username, self._gp, "GP")
        return ""
