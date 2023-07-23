from Entity.Weapon.Weapon import Weapon
from ursina import *
from Graphics.TextStyles.DamageText import DamageText


class Knife(Weapon):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Knife"

    @property
    def star_rating(self) -> int:
        return 1

    @property
    def base_attack(self) -> int:
        return 10

    @property
    def base_speed(self):
        return 0.6

    @property
    def range(self):
        return 1

    @property
    def weapon_type(self) -> str:
        return "Knife"

    @property
    def texture(self) -> str:
        return "Textures/knife.png"

    def attack_process(self, direction):
        self._instance = Entity(
            model='quad',
            texture=self.texture,
            scale=(1, 1),
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

            hit_info = raycast(self._instance.world_position, self._instance.up, ignore=[self, self._equipped_entity], distance=self.range, debug=False)
            if hit_info.hit:
                if isinstance(hit_info.entity, type(self._equipped_entity)) and hit_info.entity not in self.hit_list:
                    self.hit_list.append(hit_info.entity)
                try:
                    hit_entity = hit_info.entity
                    if hit_entity not in self.hit_list:
                        is_crit = random.randint(0, 100) < self._equipped_entity.stats.crit_rate.get_value()
                        crit_damage = (self._equipped_entity.stats.attack.get_value() * (self._equipped_entity.stats.crit_damage.get_value() * 0.01)) if is_crit else 1
                        damage = self.damage + int(round(self._equipped_entity.stats.attack.get_value() + crit_damage))
                        amount = damage - hit_entity.stats.defense.get_value()
                        DamageText(amount, is_crit, parent=hit_entity)
                        hit_entity.damage(amount)
                        self.hit_list.append(hit_entity)
                except AttributeError:
                    pass
