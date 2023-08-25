from Entity.Weapon.SwingWeapon import SwingWeapon
from Entity.Buff import Buff
from Graphics.TextStyles.DamageText import DamageText
from ursina import *


class BraydensOsuPen(SwingWeapon):
    def __init__(self):
        super().__init__(
            buff=Buff('CritDamage', True)
        )

    @property
    def name(self) -> str:
        return "Brayden's Osu Pen"

    @property
    def description(self) -> str:
        return "The pen that brayden uses to click circles"

    @property
    def base_attack(self) -> int:
        return 50

    @property
    def base_speed(self):
        return 1

    @property
    def range(self):
        return 1

    @property
    def weapon_type(self) -> str:
        return "Pen"

    @property
    def star_rating(self) -> int:
        return 5

    @property
    def texture(self) -> str:
        return "Textures/Weapon.png"
