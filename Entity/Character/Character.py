from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead


class Character(GameUnit):

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
        self.stats.health.set_default_value(int((calculate(self.experience.level, 57) + calculate(self.experience.level,
                                                                                                  calculate(
                                                                                                      self.star_rating,
                                                                                                      2)) + calculate(
            self.experience.level, calculate(self.check_minimum(self.stats.health.points, 4)))) + calculate(
            self.difficulty, 1000) + calculate(self.stats.health.points, 10) + calculate(self.star_rating, 5)))

        # attack stats
        self.stats.attack.set_default_value(int((calculate(self.experience.level, 1.25) + calculate(self.star_rating,
                                                                                                    1.50) + calculate(
            self.star_rating, calculate(self.check_minimum(self.stats.attack.points))) + calculate(
            self.difficulty - 1, 20)) + 45 + calculate(self.check_minimum(self.stats.attack.points, 3)) + calculate(
            self.star_rating, 3)))

        # defense stats
        self.stats.defense.set_default_value(
            int((calculate(self.experience.level, 2.25) + calculate(self.star_rating, 2.50) + calculate(
                self.star_rating, calculate(self.check_minimum(self.stats.defense.points)))) + calculate(50,
                                                                                                   self.difficulty) + calculate(
                self.check_minimum(self.stats.defense.points, 3)) + calculate(self.star_rating, 3)))

        # crit rate stats
        self.stats.crit_rate.set_default_value(5 + self.stats.crit_rate.points)

        # crit damage stats
        self.stats.crit_damage.set_default_value(100 + calculate(self.stats.crit_damage.points, 5))

        # speed stats
        self.stats.speed.set_default_value(self.difficulty + self.stats.speed.points)

    def update(self):
        self.set_idle_texture()
        if held_keys['left arrow']:
            self.move_left()
        elif held_keys['right arrow']:
            self.move_right()
        if held_keys['up arrow']:
            self.move_up()
        elif held_keys['down arrow']:
            self.move_down()
        elif held_keys["-"]:
            if self.experience.level > 1:
                self.experience.level -= 1
                self.update_stats()
        elif held_keys["="]:
            self.level_up()
        elif held_keys["/"]:
            self.damage(5)