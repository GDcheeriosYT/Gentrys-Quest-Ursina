from utils.Event import Event


class ScoreManager():
    def __init__(self):
        self._score = 0
        self._points = 0
        self.on_score = Event('OnScore')

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
        self.add_score(10)

    def add_kill(self):
        self.add_score(100)
