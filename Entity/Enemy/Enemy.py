import random

from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping


class Enemy(GameUnit):
    def __init__(self, texture_mapping: TextureMapping = TextureMapping(), audio_mapping: AudioMapping = AudioMapping()):
        super().__init__(
            texture_mapping,
            audio_mapping
        )
        self.on_death += lambda: self.scripts.clear()
        self.on_death += lambda: destroy(self)

    def update_follow_script(self, player):
        rany = random.uniform(-0.5, 0.5)
        ranx = random.uniform(-0.5, 0.5)
        self.add_script(SmoothFollow(target=player, offset=(ranx, rany, 0), speed=self._stats.speed.get_value()))

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

    def input(self, key):
        if key == "l":
            self.level_up()
        elif key == "k":
            if self._experience.level > 1:
                self._experience.level -= 1