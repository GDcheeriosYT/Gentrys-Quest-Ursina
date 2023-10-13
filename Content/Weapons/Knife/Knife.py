from ursina import *

from Entity.Weapon.PokeWeapon import PokeWeapon
from Entity.Buff import Buff


class Knife(PokeWeapon):
    def __init__(self):
        super().__init__(
            Buff()
        )

    @property
    def name(self) -> str:
        return "Knife"

    @property
    def star_rating(self) -> int:
        return 1

    @property
    def base_attack(self) -> int:
        return 20

    @property
    def base_speed(self):
        return 0.6

    @property
    def range(self):
        return 1.1

    @property
    def weapon_type(self) -> str:
        return "Knife"

    @property
    def texture(self) -> str:
        return "Textures/knife.png"

    @property
    def drop_chance(self) -> int:
        return 30
