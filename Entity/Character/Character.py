from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead


class Character(GameUnit):
    def __init__(self):
        super().__init__()

    @property
    def star_rating(self) -> int:
        raise NotImplementedError

    @property
    def overhead(self) -> EntityOverhead:
        return EntityOverhead(self.name, self.stats.health.get_value(), True)

    def update_stats(self):
        def calculate(variable, multiplier: Union[int, float] = 1):
            return variable * multiplier

        # experience stats
        self.difficulty = int(1 + (self.experience.level / 20))

        # health stats
        self.stats.health.set_default_value(self.experience.level * 5)

        # attack stats
        self.stats.attack.set_default_value(self.experience.level * 5)

        # defense stats
        self.stats.defense.set_default_value(self.experience.level * 5)

        # crit rate stats
        self.stats.crit_rate.set_default_value(5 + self.stats.crit_rate.points)

        # crit damage stats
        self.stats.crit_damage.set_default_value(100 + calculate(self.stats.crit_damage.points, 5))

        # speed stats
        self.stats.speed.set_default_value(self.difficulty + self.stats.speed.points + (self.star_rating * 0.10))

    def update(self):
        self.set_idle_texture()
        if held_keys['left arrow']:
            self.move_left()
        if held_keys['right arrow']:
            self.move_right()
        if held_keys['up arrow']:
            self.move_up()
        if held_keys['down arrow']:
            self.move_down()
        if held_keys["-"]:
            print("pressed -")
            if self.experience.level > 1:
                self.experience.level -= 1
        if held_keys["="]:
            print("pressed =")
            self.level_up()
        if held_keys["/"]:
            self.damage(5)
