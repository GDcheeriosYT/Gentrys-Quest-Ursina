class Experience:
    def __init__(self):
        self.xp = 0
        self.level = 1
        self.limit = None

    def get_xp_required(self, star_rating):
        if self.level != self.limit:
            return int((((self.level * 2) * 75) + ((star_rating * (self.level * 0.25)) * 25)) * ((self.level / 20) + 1))
        else:
            return self.xp

    def __repr__(self):
        return f"level {self.level}{f'/{self.limit}' if self.limit else ''} {self.xp}xp"
