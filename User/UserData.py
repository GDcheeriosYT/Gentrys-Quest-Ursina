from ursina import *
from typing import List

import Game
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact
from Entity.Weapon.Weapon import Weapon
from Overlays.NotificationsManager import NotificationManager
from Overlays.Notification import Notification
from IO.DataLoader import DataLoader
import json


class UserData:
    def __init__(self, json_str: str = None):
        if json_str:
            json_data = json.loads(json_str)
            self._characters = DataLoader.parse_characters(json_data["inventory"]["characters"])
            self._artifacts = DataLoader.parse_characters(json_data["inventory"]["artifacts"])
            self._weapons = DataLoader.parse_characters(json_data["inventory"]["weapons"])
            self._items = []
            self._equipped_character = None
            self._money = json_data["inventory"]["money"]
            self._startup_amount = json_data["startup amount"]
        else:
            self._characters = []
            self._artifacts = []
            self._items = []
            self._equipped_character = None
            self._weapons = []
            self._money = 0
            self._startup_amount = 0

    @property
    def characters(self) -> List[Character]:
        return self._characters

    @property
    def artifacts(self) -> List[Artifact]:
        return self._artifacts

    @property
    def weapons(self) -> List[Weapon]:
        return self._weapons

    @property
    def items(self):
        return self._items

    @property
    def money(self):
        return self._money

    @property
    def startup_amount(self):
        return self._startup_amount

    @property
    def equipped_character(self) -> Character:
        return self._equipped_character

    def add_character(self, character: Character):
        Game.notification_manager.add_notification(Notification(f"obtained {character.star_rating} star {character.name} character", color=color.blue))
        self._characters.append(character)

    def add_artifact(self, artifact: Artifact):
        Game.notification_manager.add_notification(Notification(f"obtained {artifact.star_rating} star {artifact.name} artifact", color=color.blue))
        self._artifacts.append(artifact)

    def add_weapon(self, weapon: Weapon):
        Game.notification_manager.add_notification(Notification(f"obtained {weapon.star_rating} star {weapon.name} weapon", color=color.blue))
        self._weapons.append(weapon)

    def add_money(self, money: int):
        self._money += money

    def remove_money(self, money: int):
        self._money -= money

    def equip_character(self, character: Character):
        if self._equipped_character:
            self.equipped_character.unequip()

        self._equipped_character = character
        self._equipped_character.equip()

    def increment_startup_amount(self):
        self._startup_amount += 1

    def jsonify_data(self) -> dict:
        characters = [character.jsonify() for character in self._characters]
        artifacts = [artifact.jsonify() for artifact in self._artifacts]
        weapons = [weapon.jsonify() for weapon in self._weapons]

        return {
            "startup amount": self._startup_amount,
            "inventory": {
                "characters": characters,
                "artifacts": artifacts,
                "weapons": weapons,
                "money": self._money
            }
        }

    def __repr__(self):
        print(self._startup_amount)
        print(f"${self._money}")
        print(self._characters)
        print(self._artifacts)
        print(self._weapons)
        return ""
