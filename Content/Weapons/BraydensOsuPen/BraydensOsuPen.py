    from Entity.Weapon.Weapon import Weapon
from ursina import *
from ursina.curve import *


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
    def base_speed(self):
        return 1.5

    @property
    def weapon_type(self) -> str:
        return "Pen"

    @property
    def weapon_texture(self) -> str:
        return "Textures/Weapon.png"

    def attack_process(self, damage, speed):
        weapon = Entity(
            model='quad',
            texture=self.weapon_texture,
            scale=(1, 1)
        )

        center = (0, 0, 0)

        weapon.x += 1.5
        weapon.rotation_z = 30

        speed = self.base_speed/speed
        destroy(weapon, speed + 0.01)
