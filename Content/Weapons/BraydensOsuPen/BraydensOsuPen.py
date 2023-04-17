from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.WeaponTypes import WeaponTypes


class BraydensOsuPen(Weapon):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Braydens Osu Pen"

    @property
    def base_attack(self) -> int:
        return 50

    @property
    def weapon_type(self) -> str:
        return "Pen"
