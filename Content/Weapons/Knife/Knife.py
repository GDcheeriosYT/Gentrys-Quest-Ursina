from Entity.Weapon.Weapon import Weapon
from ursina import *


class Knife(Weapon):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Knife"

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
    def weapon_texture(self) -> str:
        return "Textures/knife.png"

    def attack_process(self, direction):
        self._instance = Entity(
            model='quad',
            texture=self.weapon_texture,
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
                    is_crit = random.randint(0, 100) < self._equipped_entity.stats.crit_rate.get_value()
                    crit_damage = (self._equipped_entity.stats.attack.get_value() * (
                                self._equipped_entity.stats.crit_damage.get_value() * 0.01)) if is_crit else 1
                    damage = self.base_attack + int(round(self._equipped_entity.stats.attack.get_value() + crit_damage))
                    if hit_entity not in self.hit_list:
                        amount = damage - hit_entity.stats.defense.get_value()
                        damage_text = Text(str(amount if amount > 0 else "miss"), scale=(20, 20), position=(0, 0.5, -1),
                                           origin=(0, 0), color=color.red if is_crit else color.white,
                                           parent=hit_info.entity)
                        damage_text.animate_position((damage_text.x + 0.1, damage_text.y + 0.5), 1)
                        damage_text.fade_out(0, 1)
                        destroy(damage_text, delay=1.5)
                        hit_entity.damage(amount)
                        self.hit_list.append(hit_info.entity)
                        print(f"{'critical ' if is_crit else ''}hit {hit_info.entity} for {self.damage}")
                except AttributeError:
                    pass
