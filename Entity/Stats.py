from .Stat import Stat


class Stats:
    def __init__(self):
        self.health = Stat("Health", 100)
        self.attack = Stat("Attack")
        self.defense = Stat("Defense")
        self.crit_rate = Stat("CritRate", 5.00)
        self.crit_damage = Stat("CritDamage", 100.00)
        self.speed = Stat("Speed")

    def __repr__(self):
        print(self.health)
        print(self.attack)
        print(self.defense)
        print(self.crit_rate)
        print(self.crit_damage)
        print(self.speed)
