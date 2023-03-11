from ursina import *
from ..GameUnit import GameUnit
from ..Stats import Stats
from ursina.prefabs.health_bar import HealthBar
from typing import Union
from ..TextureMapping import TextureMapping


class Character(GameUnit):

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
            self.experience.level, calculate(self.check_minimum(self.health_points, 4)))) + calculate(
            self.difficulty, 1000) + calculate(self.health_points, 10) + calculate(self.star_rating, 5)))

        # attack stats
        self.stats.attack.set_default_value(int((calculate(self.experience.level, 1.25) + calculate(self.star_rating,
                                                                                                    1.50) + calculate(
            self.star_rating, calculate(self.check_minimum(self.attack_points))) + calculate(
            self.difficulty - 1, 20)) + 45 + calculate(self.check_minimum(self.attack_points, 3)) + calculate(
            self.star_rating, 3)))

        # defense stats
        self.stats.defense.set_default_value(
            int((calculate(self.experience.level, 2.25) + calculate(self.star_rating, 2.50) + calculate(
                self.star_rating, calculate(self.check_minimum(self.defense_points)))) + calculate(50,
                                                                                                   self.difficulty) + calculate(
                self.check_minimum(self.defense_points, 3)) + calculate(self.star_rating, 3)))

        # crit rate stats
        self.stats.crit_rate.set_default_value(5 + self.crit_rate_points)

        # crit damage stats
        self.stats.crit_damage.set_default_value(100 + calculate(self.crit_damage_points, 5))

        # speed stats
        self.stats.speed.set_default_value(self.difficulty + self.speed_points)

    def update(self):
        if held_keys['left arrow']:
            self.x -= self.stats.speed.get_value() * time.dt
        elif held_keys['right arrow']:
            self.x += self.stats.speed.get_value() * time.dt
        if held_keys['up arrow']:
            self.y += self.stats.speed.get_value() * time.dt
        elif held_keys['down arrow']:
            self.y -= self.stats.speed.get_value() * time.dt
        elif held_keys["-"]:
            if self.experience.level > 1:
                self.experience.level -= 1
                self.update_stats()
        elif held_keys["="]:
            self.level_up()
        elif held_keys["/"]:
            self.damage(5)