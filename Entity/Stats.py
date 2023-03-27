from .Stat import Stat


class Stats:

    @property
    def health(self) -> Stat:
        return Stat("Health", 100)

    @property
    def attack(self) -> Stat:
        return Stat("Attack")

    @property
    def defense(self) -> Stat:
        return Stat("Defense")

    @property
    def crit_rate(self) -> Stat:
        return Stat("CritRate", 5.00)

    @property
    def crit_damage(self) -> Stat:
        return Stat("CritDamage", 100.00)

    @property
    def speed(self) -> Stat:
        return Stat("Speed")

    def __repr__(self):
        print(self.health)
        print(self.attack)
        print(self.defense)
        print(self.crit_rate)
        print(self.crit_damage)
        print(self.speed)
        return ""
