from ursina import *
from ..GameEntity import GameEntity
from ..Stats import Stats
from ursina.prefabs.health_bar import HealthBar
from typing import Union
from ..TextureMapping import TextureMapping


class Character(GameEntity):
    def __init__(self, name: str, star_rating: int, health_points: int = 0, attack_points: int = 0, defense_points=0,
                 crit_rate_points: int = 0, crit_damage_points: int = 0, speed_points: int = 0,
                 texture_mapping: TextureMapping = TextureMapping()):
        if star_rating > 5:
            star_rating = 5
        elif star_rating < 1:
            star_rating = 1
        else:
            star_rating = star_rating

        super().__init__(
            name,
            star_rating,
            texture_mapping
        )

        self.health_points = health_points
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.crit_rate_points = crit_rate_points
        self.crit_damage_points = crit_damage_points
        self.speed_points = speed_points

        self.stats = Stats()

        self.name_tag = Entity(model=Text(self.name), parent=self, y=self.scale_y / 2 + 0.1)

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

    def damage(self, amount):
        self.health -= amount
        self.on_damage()

    def on_damage(self):
        if self.stats.health.current_value <= 0:
            self.on_death()

    def on_death(self):
        self.revive()

    def revive(self):
        self.health = self.stats.health.get_value()

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
