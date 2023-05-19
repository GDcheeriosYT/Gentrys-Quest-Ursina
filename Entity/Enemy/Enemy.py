import random

from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from Entity.Loot import Loot


class Enemy(GameUnit):
    def __init__(self, texture_mapping: TextureMapping = TextureMapping(), audio_mapping: AudioMapping = AudioMapping()):
        super().__init__(
            texture_mapping,
            audio_mapping
        )

        self._follow_entity = None

        self.on_death += lambda: destroy(self)
        self.on_level_up += lambda: self._overhead.change_name(self.name + f"\nlevel {self.experience.level}")

    def follow_entity(self, entity: Entity):
        self._follow_entity = entity

    def update_stats(self):
        def calculate(variable, multiplier: Union[int, float] = 1):
            return variable * multiplier

        # experience stats
        self._difficulty = int(1 + (self.experience.level / 20))

        # health stats
        self._stats.health.set_default_value(int(calculate(500, self._difficulty) + calculate(self.experience.level, (5 + calculate(self.experience.level, 0.18 + calculate(self._difficulty, 0.09))) + calculate(self.stats.health.points, 5))))

        # attack stats
        self._stats.attack.set_default_value(int(calculate(30, self._difficulty) + calculate(self.experience.level, (calculate(self.experience.level, 0.04 + calculate(self._difficulty, 0.007))) + calculate(self.stats.attack.points, 2))))

        # defense stats
        self._stats.defense.set_default_value(int(calculate(35, self._difficulty) + calculate(self.experience.level, (calculate(self.experience.level, 0.03 + calculate(self._difficulty, 0.006))) + calculate(self.stats.defense.points, 2))))

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
        money += self.experience.level * 2

        xp = 0
        xp += self._stats.defense.points * 0.5
        xp += self._stats.attack.points * 1.5
        xp += self._stats.health.points * 1
        xp += self.experience.level * 25

        return Loot(
            xp,
            money
        )

    def update(self):
        self.direction = Vec3(self._follow_entity.position - self.position).normalized()  # get the direction we're trying to walk in.
        origin = self.world_position
        hit_info = raycast(origin, self.direction, ignore=[self], distance=.5)
        self.attack(self.direction)
        if not hit_info.hit:
            if self.can_move:
                self.position += self.direction * self._stats.speed.get_value() * time.dt
                self.on_move()

        if held_keys['o']:
            self.damage(self.experience.level * 50)

        if held_keys["l"]:
            self.level_up()
        elif held_keys["k"]:
            if self._experience.level > 1:
                self._experience.level -= 1

            self.on_level_up()
