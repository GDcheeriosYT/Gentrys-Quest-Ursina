import random

from .GachaTypes import GachaTypes

from typing import List
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon


class Gacha:
    def __init__(self, name: str, characters: List[Character], weapons: List[Weapon]):
        self.name = name
        self.characters = characters
        self.weapons = weapons

    def pull(self, amount: int, type: GachaTypes):
        pulled = []
        amount_pulled = 0

        while amount_pulled < amount:
            character = random.choice(self.characters)
            random_value = random.randint(0, 10000)
            star_rating = 1
            if random_value <= 100:
                star_rating = 5

            elif random_value <= 500:
                star_rating = 4

            elif random_value <= 1000:
                star_rating = 3

            elif random_value <= 5000:
                star_rating = 2

            if star_rating >= character.star_rating:
                pulled.append(character)

            if type == GachaTypes.Character:
                pass

            if type == GachaTypes.Weapon:
                pass
