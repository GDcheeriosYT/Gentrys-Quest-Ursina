import Game
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
        self._gp = Game.rating_program.rater.generate_power_details(self._user_data.jsonify_data(), True)['rating']['weighted']

    @property
    def username(self) -> str:
        return self._username

    @property
    def user_data(self) -> UserData:
        return self._user_data

    @property
    def gp(self) -> int:
        return self._gp

    def get_equipped_character(self) -> Character:
        return self._user_data.equipped_character

    def get_money(self) -> int:
        return self._user_data.money

    def get_characters(self) -> List[Character]:
        return self._user_data.characters

    def get_artifacts(self) -> List[Artifact]:
        return self._user_data.artifacts

    def get_weapons(self) -> List[Weapon]:
        return self._user_data.weapons

    def replace_data(self, json_str):
        self._user_data = UserData(json_str)

    def add_character(self, character: Character):
        self._user_data.add_character(character)

    def add_artifact(self, artifact: Artifact):
        self._user_data.add_artifact(artifact)

    def add_weapon(self, weapon: Weapon):
        self._user_data.add_weapon(weapon)

    def add_money(self, money: int):
        self._user_data.add_money(money)

    def equip_character(self, character: Character):
        self._user_data.equip_character(character)

    def unload(self):
        if self._is_guest:
            json.dump(self._user_data.jsonify_data(), open(f"Data/{self._username}.json", "w"), indent=4)

    def __repr__(self):
        print(self._username, self._gp, "GP")
        return ""
