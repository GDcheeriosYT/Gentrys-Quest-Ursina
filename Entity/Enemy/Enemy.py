import random

from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from Entity.Loot import Loot
from Entity.Affiliation import Affiliation


class Enemy(GameUnit):
    def __init__(self, texture_mapping: TextureMapping = TextureMapping(), audio_mapping: AudioMapping = AudioMapping(), *args, **kwargs):
        super().__init__(
            texture_mapping,
            audio_mapping,
            *args,
            **kwargs
        )
        self.set_idle_texture()
        self.affiliation = Affiliation.Enemy

        self._follow_entity = None
        self.not_attacking = True

        self.on_level_up += lambda: self._overhead.change_name(self.name + f"\nlevel {self.experience.level}")

    @property
    def attack_delay(self) -> Union[int, float]:
        return 1

    def follow_entity(self, entity: Entity):
        self._follow_entity = entity

    def update_stats(self):
        def calculate(variable, multiplier: Union[int, float] = 1):
            return variable * multiplier

        # experience stats
        self._difficulty = int(1 + (self.experience.level / 20))

        # health stats
        self._stats.health.set_default_value(int(calculate(500, self._difficulty) + calculate(self.experience.level, (5 + calculate(self.experience.level, 0.2 + calculate(self._difficulty, 0.18))) + calculate(self.stats.health.points, 7))))

        # attack stats
        self._stats.attack.set_default_value(int(calculate(250, self._difficulty) + calculate(self.experience.level, (calculate(self.experience.level, 0.06 + calculate(self._difficulty, 0.014))) + calculate(self.stats.attack.points, 4))))

        # defense stats
        self._stats.defense.set_default_value(int(calculate(5, self._difficulty) + calculate(self.experience.level, (calculate(self.experience.level, 0.03 + calculate(self._difficulty, 0.012))) + calculate(self.stats.defense.points, 2))))

        # crit rate stats
        self._stats.crit_rate.set_default_value(20)

        # crit damage stats
        self._stats.crit_damage.set_default_value(calculate(self.stats.crit_damage.points, 5))

        # speed stats
        self._stats.speed.set_default_value(((self.difficulty - 1) * 0.2) + self.stats.speed.points)

    def get_loot(self) -> Loot:
        money = 0
        money += self._stats.defense.points * 1.5
        money += self._stats.attack.points * 2.5
        money += self._stats.health.points * 2
        money += self.experience.level * 1.2
        money = int(money)

        xp = 0
        xp += self._stats.defense.points * 0.5
        xp += self._stats.attack.points * 1.5
        xp += self._stats.health.points * 1
        xp += self.experience.level * 25

        return Loot(
            xp,
            money
        )

    def attack_switch(self, on: bool):
        self.not_attacking = on

    def attack(self, direction=None):
        self.not_attacking = False
        invoke(lambda: self.attack_switch(True), delay=self.attack_delay)
        if self._weapon:
            if self._weapon.is_ready():
                if not direction:
                    mouse_pos = mouse.position
                    direction = math.atan2(mouse_pos[1], mouse_pos[0]) * (180 / 3.14)
                else:
                    direction = math.atan2(direction[1], direction[0]) * (180 / 3.14)

                self.on_attack()
                self.weapon.attack(direction)

    def update(self):
        if self.not_attacking and self._follow_entity:
            self.direction = Vec3(self._follow_entity.position - self.position).normalized()  # get the direction we're trying to walk in.
            if sqrt((self._follow_entity.position[0] - self.position[0]) ** 2 + (self._follow_entity.position[1] - self.position[1]) ** 2) <= self.range:
                self.attack(self.direction)

            if not self.is_effected_by("Stun") and not self.hits(self.direction):
                self.position += self.direction * self._stats.speed.get_value() * time.dt
                self.on_move()
