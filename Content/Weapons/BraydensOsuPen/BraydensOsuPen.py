from Entity.Weapon.Weapon import Weapon
from ursina import *


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
        return 1

    @property
    def range(self):
        return 1

    @property
    def weapon_type(self) -> str:
        return "Pen"

    @property
    def weapon_texture(self) -> str:
        return "Textures/Weapon.png"

    def attack_process(self):
        self._instance = Entity(
            model='quad',
            texture=self.weapon_texture,
            scale=(1, 1),
            origin=(0, 0.5),
            parent=self._equipped_entity
        )

        self.hit_list = []
        self.time_started = time.time()
        self.speed = self.base_speed/self._equipped_entity.stats.attack_speed.get_value()
        invoke(self.destroy_instance, delay=(self.speed + 0.01))

    def update(self):
        if self._instance:
            x = 0.7
            y = 1
            angle = -90
            time_elapsed = (time.time() - self.time_started)
            self._instance.rotation_z = (angle - (-angle - angle) * (time_elapsed / self.speed))
            self._instance.y = y * (1 - abs(time_elapsed / self.speed - 0.5) * 2)
            self._instance.x = (x + (-x - x) * (time_elapsed / self.speed))
            hit_info = raycast(self._instance.world_position, self._instance.down, ignore=[self, self._equipped_entity], distance=self.range, debug=False)
            if hit_info.hit:
                try:
                    hit_entity = hit_info.entity
                    is_crit = random.randint(0, 100) < self._equipped_entity.stats.crit_rate.get_value()
                    crit_damage = (self._equipped_entity.stats.attack.get_value() * (self._equipped_entity.stats.crit_damage.get_value() * 0.01)) if is_crit else 1
                    damage = self.base_attack + int(round(self._equipped_entity.stats.attack.get_value() + crit_damage))
                    if hit_entity not in self.hit_list:
                        amount = damage - hit_entity.stats.defense.get_value()
                        damage_text = Text(str(amount if amount > 0 else "miss"), scale=(20, 20), position=(0, 0.5, -1), origin=(0, 0), color=color.red if is_crit else color.white, parent=hit_info.entity)
                        damage_text.animate_position((damage_text.x + 0.1, damage_text.y + 0.5), 1)
                        damage_text.fade_out(0, 1)
                        destroy(damage_text, delay=1.5)
                        hit_entity.damage(damage)
                        self.hit_list.append(hit_info.entity)
                        print(f"{'critical ' if is_crit else ''}hit {hit_info.entity} for {self.damage}")
                except AttributeError:
                    pass

