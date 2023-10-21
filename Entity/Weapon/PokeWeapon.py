from Entity.Weapon.Weapon import Weapon
from Entity.Buff import Buff
from Graphics.TextStyles.DamageText import DamageText
from ursina import *


class PokeWeapon(Weapon):
    def __init__(self, buff: Buff):
        super().__init__(
            buff
        )

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def description(self) -> str:
        return ""

    @property
    def base_attack(self) -> int:
        raise NotImplementedError

    @property
    def base_speed(self) -> int:
        raise NotImplementedError

    @property
    def weapon_type(self) -> str:
        raise NotImplementedError

    @property
    def texture(self) -> str:
        raise NotImplementedError

    @property
    def star_rating(self) -> int:
        raise NotImplementedError

    @property
    def range(self) -> int:
        raise NotImplementedError

    def attack_process(self, direction):
        self._instance = Entity(
            model='quad',
            texture=self.texture,
            scale=self.scale_override,
            origin=(0, -0.5),
            rotation=(0, 0, -direction + 90),
            parent=self._equipped_entity
        )

        self.time_started = time.time()
        self.hit_list = []
        self.speed = self.base_speed / self._equipped_entity.stats.attack_speed.get_value()
        self.angle = direction
        invoke(self.destroy_instance, delay=(self.speed + 0.01))

    def update(self):
        if self._instance:
            time_elapsed = (time.time() - self.time_started)
            progress = time_elapsed / self.speed
            if progress <= 0.5:
                progress_normalized = (progress / 0.5)
                angle_radians = math.radians(self.angle)
                distance = progress_normalized * (self.range / 2)
                x_offset = math.cos(angle_radians) * distance
                y_offset = math.sin(angle_radians) * distance
            else:
                progress_normalized = ((1.0 - progress) / 0.5)
                angle_radians = math.radians(self.angle)
                distance = progress_normalized * (self.range / 2)
                x_offset = math.cos(angle_radians) * distance
                y_offset = math.sin(angle_radians) * distance

            self._instance.position = Vec3(x_offset, y_offset, 0)
            self.manage_collision(False)