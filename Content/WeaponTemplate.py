from Entity.Weapon.Weapon import Weapon
from ursina import *


class WeaponName(Weapon):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Weapon Name"

    @property
    def base_attack(self) -> int:
        return 10

    @property
    def base_speed(self):
        return 1

    @property
    def range(self):
        return 1

    @property
    def weapon_type(self) -> str:
        return "Weapon Type"

    @property
    def texture(self) -> str:
        return "Textures/texturename.fileformat"

    @property
    def star_rating(self) -> int:
        return 1

    def attack_process(self, direction):
        self._instance = Entity(
            model='quad',
            texture=self.texture,
            scale=(1, 1),
            origin=(0, 0.5),
            parent=self._equipped_entity
        )

        self.time_started = time.time()
        self.speed = self.base_speed / self._equipped_entity.stats.attack_speed.get_value()
        self.angle = direction
        invoke(self.destroy_instance, delay=(self.speed + 0.01))

    def update(self):
        if self._instance:
            time_elapsed = (time.time() - self.time_started)
            progress = time_elapsed / self.speed
            pass
