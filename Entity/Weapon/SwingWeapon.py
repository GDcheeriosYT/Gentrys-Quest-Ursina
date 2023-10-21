from Entity.Weapon.Weapon import Weapon
from Entity.Buff import Buff
from Graphics.TextStyles.DamageText import DamageText
from ursina import *


class SwingWeapon(Weapon):
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
            origin=(0, 0.5),
            parent=self._equipped_entity
        )

        self.hit_list = []
        self.time_started = time.time()
        self.speed = self.base_speed/self._equipped_entity.stats.attack_speed.get_value()
        self.angle = direction
        invoke(self.destroy_instance, delay=(self.speed + 0.01))

    def update(self):
        if self._instance:
            pivot_point = Vec3(0, 0, 0)
            swing_distance = 1
            time_elapsed = (time.time() - self.time_started)
            angle = (self.angle - 90) + (180 * (time_elapsed / self.speed))
            radian = math.radians(angle)
            x_offset = math.cos(radian) * swing_distance
            y_offset = math.sin(radian) * swing_distance
            self._instance.rotation_z = -angle - 90
            self._instance.position = pivot_point + Vec3(x_offset, y_offset, 0)
            self._instance.y = y_offset
            self.manage_collision()
