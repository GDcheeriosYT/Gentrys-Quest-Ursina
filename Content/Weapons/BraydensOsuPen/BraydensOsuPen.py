from Entity.Weapon.Weapon import Weapon
from Entity.Buff import Buff
from Graphics.TextStyles.DamageText import DamageText
from ursina import *


class BraydensOsuPen(Weapon):
    def __init__(self):
        super().__init__(
            buff=Buff('CritDamage', True)
        )

    @property
    def name(self) -> str:
        return "Braydens Osu Pen"

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

    def attack_process(self, direction):
        self._instance = Entity(
            model='quad',
            texture=self.texture,
            scale=(1, 1),
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
            hit_info = raycast(self._instance.world_position, self._instance.down, ignore=[self, self._equipped_entity], distance=self.range, debug=False)
            if hit_info.hit:
                try:
                    hit_entity = hit_info.entity
                    is_crit = random.randint(0, 100) < self._equipped_entity.stats.crit_rate.get_value()
                    crit_damage = (self._equipped_entity.stats.attack.get_value() * (self._equipped_entity.stats.crit_damage.get_value() * 0.01)) if is_crit else 1
                    damage = self.damage + int(round(self._equipped_entity.stats.attack.get_value() + crit_damage))
                    if hit_entity not in self.hit_list:
                        amount = damage - hit_entity.stats.defense.get_value()
                        DamageText(amount, is_crit, parent=hit_info.entity)
                        hit_entity.damage(amount)
                        self.hit_list.append(hit_info.entity)
                except AttributeError:
                    pass

