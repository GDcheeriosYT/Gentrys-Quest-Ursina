from Entity.Stats import Stats
import random


class Buff:
    def __init__(self, stat: str = "Random", is_percent: bool = None):
        if stat == "Random":
            stat = random.choice(Stats.get_stat_strings())
        self._stat = stat
        self._value = 0
        if not is_percent:
            self._is_percent = random.choice([True, False])
        else:
            self._is_percent = is_percent
        self._level = 1

    def handle_value(self, star_rating):
        calculation = ((self._level * 1.75) + (star_rating * 1.25) + (star_rating * int(self._level / star_rating)))
        if self._stat == "CritRate":
            calculation /= 4
        self._value = int(calculation) if not self.is_percent else float(calculation)

    @property
    def stat(self) -> str:
        return self._stat

    @property
    def is_percent(self) -> bool:
        return self._is_percent

    @property
    def value(self):
        return self._value

    @property
    def level(self) -> int:
        return self._level
