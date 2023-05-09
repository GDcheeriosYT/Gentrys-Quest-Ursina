from .Stat import Stat


class Stats:
    def __init__(self):
        self._health = Stat("Health", 100)
        self._attack = Stat("Attack", 16)
        self._defense = Stat("Defense", 12)
        self._crit_rate = Stat("CritRate", 5)
        self._crit_damage = Stat("CritDamage", 50)
        self._speed = Stat("Speed", 3)

    @property
    def health(self) -> Stat:
        return self._health

    @property
    def attack(self) -> Stat:
        return self._attack

    @property
    def defense(self) -> Stat:
        return self._defense

    @property
    def crit_rate(self) -> Stat:
        return self._crit_rate

    @property
    def crit_damage(self) -> Stat:
        return self._crit_damage

    @property
    def speed(self) -> Stat:
        return self._speed

    @staticmethod
    def get_stat_strings() -> list:
        return [
            "Health",
            "Attack",
            "Defense",
            "CritRate",
            "CritDamage",
            "Speed",
        ]

    def get_stat_by_string(self, string: str):
        if string == "Health":
            return self._health
        elif string == "Attack":
            return self._attack
        elif string == "Defense":
            return self._defense
        elif string == "CritRate":
            return self._crit_rate
        elif string == "CritDamage":
            return self._crit_damage
        elif string == "Speed":
            return self._speed

    def __repr__(self):
        return f'''
{self.health}
{self.attack}
{self.defense}
{self.crit_rate}
{self.crit_damage}
{self.speed}
        '''
