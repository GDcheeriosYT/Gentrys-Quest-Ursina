from ursina import *
from ursina.camera import Camera

from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead
from Content.Enemies.TestEnemy import TestEnemy
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping


class Character(GameUnit):
    def __init__(self, texture_mapping: TextureMapping = TextureMapping(), audio_mapping: AudioMapping = AudioMapping()):
        super().__init__(
            texture_mapping=texture_mapping,
            audio_mapping=audio_mapping
        )
        self._is_equipped = False
        self.artifacts = []
        self._overhead.disable()

    @property
    def star_rating(self) -> int:
        raise NotImplementedError

    @property
    def is_equipped(self) -> bool:
        return self._is_equipped

    def update_stats(self):
        def calculate(variable, multiplier: Union[int, float] = 1):
            return variable * multiplier

        # experience stats
        self._difficulty = int(1 + (self.experience.level / 20))

        # health stats
        self._stats.health.set_default_value(int((calculate(self._experience.level, 57) + calculate(self._experience.level, calculate(self.star_rating, 2)) + calculate(self._experience.level, calculate(self.check_minimum(self._stats.health.points, 4)))) + calculate(self._difficulty, 1000) + calculate(self._stats.health.points, 10) + calculate(self.star_rating, 5)))

        # attack stats
        self._stats.attack.set_default_value(int((calculate(self._experience.level, 1.25) + calculate(self.star_rating, 1.50) + calculate(self.star_rating, calculate(self.check_minimum(self._stats.attack.points))) + calculate(self.difficulty - 1, 20)) + 45 + calculate(self.check_minimum(self._stats.attack.points, 3)) + calculate(self.star_rating, 3)))

        # defense stats
        self._stats.defense.set_default_value(self.experience.level * 5)

        # crit rate stats
        self._stats.crit_rate.set_default_value(5 + self.stats.crit_rate.points)

        # crit damage stats
        self._stats.crit_damage.set_default_value(calculate(self.stats.crit_damage.points, 5))

        # speed stats
        self._stats.speed.set_default_value(((self.difficulty - 1) * 0.2) + self.stats.speed.points + (self.star_rating * 0.1))

    def update(self):
        camera.position = (self.x, self.y, -20)
        self.set_idle_texture()
        if held_keys['a'] or held_keys['left arrow']:
            self.move_left()
        if held_keys['d'] or held_keys['right arrow']:
            self.move_right()
        if held_keys['w'] or held_keys['up arrow']:
            self.move_up()
        if held_keys['s'] or held_keys['down arrow']:
            self.move_down()
        if held_keys["-"]:
            if self.experience.level > 1:
                self.experience.level -= 1
                self.on_level_up()
                self.update_stats()
        if held_keys["="]:
            self.level_up()
        if held_keys["/"]:
            self.damage(50)

    def input(self, key):
        if key == "p":
            test_enemy = TestEnemy()
            test_enemy.position = self.position
            test_enemy.update_follow_script(self)
            test_enemy.spawn()