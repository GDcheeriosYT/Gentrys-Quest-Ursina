import random

from .GachaTypes import GachaTypes


class Gacha:
    def __init__(self, name: str, cost: int, characters: list, weapons: list):
        self.name = name
        self.cost = cost
        self.characters = [character() for character in characters]
        self.weapons = [weapon() for weapon in weapons]

    def pull(self, amount: int, type: GachaTypes):
        pulled = []
        amount_pulled = 0

        while amount_pulled < amount:
            pool = []

            def pull_thing():
                nonlocal amount_pulled
                nonlocal pool
                amount_pulled += 1

                return random.choice(pool)

            random_value = random.randint(0, 10000)
            star_rating = 1
            if random_value <= 250:
                star_rating = 5

            elif random_value <= 750:
                star_rating = 4

            elif random_value <= 1500:
                star_rating = 3

            elif random_value <= 3000:
                star_rating = 2

            if type == GachaTypes.Character:
                for character in self.characters:
                    if character.star_rating == star_rating:
                        pool.append(character)

            if type == GachaTypes.Weapon:
                for weapon in self.weapons:
                    if weapon.star_rating == star_rating:
                        pool.append(weapon)

            if len(pool) > 0:
                pulled.append(pull_thing())

        return pulled
