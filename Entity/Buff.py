from Entity.Stats import Stats
import random


class Buff:
    def __init__(self, stat: str = "Random", is_percent: bool = None):
        if stat == "Random":
            stat = random.choice(Stats.get_stat_strings())
        self._stat = stat
        self._value = 0
        if self._stat == "CritRate" or self._stat == "CritDamage" or self._stat == "Speed" or self._stat == "AttackSpeed":
            self._is_percent = False
        else:
            if is_percent is None:
                self._is_percent = random.choice([True, False])
            else:
                self._is_percent = is_percent

        self.level = 1

    def handle_value(self, star_rating, is_weapon: bool = False):
        calculation = ((self.level * 1.75) + (star_rating * 1.25) + (star_rating * int(self.level / star_rating)))
        if self._stat == "CritRate":
            calculation = self.level + (star_rating * 1.5)
        elif self._stat == "CritDamage":
            calculation * 4
        elif self._stat == "Speed":
            calculation = (star_rating * 0.05) + (self.level * 0.095)
        elif self._stat == "AttackSpeed":
            calculation = (star_rating * 0.05) + (self.level * 0.095)
        else:
            calculation *= 6

        if self._is_percent:
            calculation /= 4

        if is_weapon and self._stat != "CritRate":
            calculation /= 4

        self._value = round(calculation, 2)
        if Stats().get_stat_by_string(self._stat).is_int and not self._is_percent: self._value = int(round(self._value, 2))
        # print(self._stat, self.level, self._value, calculation)

    @property
    def stat(self) -> str:
        return self._stat

    @property
    def is_percent(self) -> bool:
        return self._is_percent

    @property
    def value(self):
        return self._value

    def level_up(self):
        self.level += 1

    def get_buff_level_string(self) -> str:
        return f"[{self.level}]"

    def jsonify(self):
        return {
            'stat': self._stat,
            'is percent': self._is_percent,
            'level': self.level
        }

    def __repr__(self):
        return f"{self._stat}{self.get_buff_level_string() if self.level > 1 else ''} {self._value}{'%' if self._is_percent else ''}\n"
