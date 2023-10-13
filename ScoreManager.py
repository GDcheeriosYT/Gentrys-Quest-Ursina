from utils.Event import Event


class ScoreManager():
    def __init__(self):
        self._score = 0
        self._points = 0
        self.on_score = Event('OnScore')

        self._hit_score = 0
        self._crit_score = 0
        self._kill_score = 0
        self._heal_score = 0
        self._damage_score = 0
        self._levels_score = 0

        # stats
        self._hits = 0
        self._crits = 0
        self._kills = 0
        self._heals = 0
        self._damage = 0
        self._levels = 0

    def get_score(self):
        return self._score

    def reset_score(self):
        self._score = 0

        self.on_score()

    def add_score(self, amount):
        self._score += amount
        self._points += amount

        self.on_score()

    def spend_points(self, amount):
        if self._points >= amount:
            self._points -= amount
            return True
        else:
            return False

    def add_hit(self):
        self._hits += 1
        amount = 10
        self.add_score(amount)
        self._hit_score += amount

    def add_crit(self):
        self._crits += 1
        amount = 40
        self.add_score(amount)
        self._crit_score += amount

    def add_kill(self):
        self._kills += 1
        amount = 100
        self.add_score(amount)
        self._kill_score = amount

    def add_heal(self, amount):
        self._heals += 1
        amount = int(amount / 20)
        self.add_score(amount)
        self._heal_score += amount


    def add_damage(self, amount):
        self._damage += amount
        amount = int(amount / 10)
        self.add_score(amount)
        self._damage_score += amount

    def add_level(self, level):
        self._levels += 1
        amount = level * 100
        self.add_score(amount)
        self._levels_score += amount
