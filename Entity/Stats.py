from .Stat import Stat


class Stats:
    def __init__(self):
        self._health = Stat("Health", 100)
        self._attack = Stat("Attack", 16)
        self._defense = Stat("Defense", 12)
        self._crit_rate = Stat("CritRate", 5)
        self._crit_damage = Stat("CritDamage", 50)
        self._speed = Stat("Speed", 2, False)
        self._attack_speed = Stat("AttackSpeed", 1, False)

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

    @property
    def attack_speed(self) -> Stat:
        return self._attack_speed

    def boost_all_stats(self, percentage):
        self._health.boost_stat(percentage)
        self._attack.boost_stat(percentage)
        self._defense.boost_stat(percentage)
        self._crit_rate.boost_stat(percentage)
        self._crit_damage.boost_stat(percentage)
        self._speed.boost_stat(percentage)
        self._attack_speed.boost_stat(percentage)

    @staticmethod
    def get_stat_strings() -> list:
        return [
            "Health",
            "Attack",
            "Defense",
            "CritRate",
            "CritDamage",
            "Speed",
            "AttackSpeed"
        ]

    def reset_additional_stats(self):
        self._health.set_additional_value(0)
        self._attack.set_additional_value(0)
        self._defense.set_additional_value(0)
        self._crit_rate.set_additional_value(0)
        self._crit_damage.set_additional_value(0)
        self._speed.set_additional_value(0)
        self._attack_speed.set_additional_value(0)

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
        elif string == "AttackSpeed":
            return self._attack_speed

    def __repr__(self):
        return f'''
{self.health}
{self.attack}
{self.defense}
{self.crit_rate}%
{self.crit_damage}%
{self.speed}
{self.attack_speed}
        '''
