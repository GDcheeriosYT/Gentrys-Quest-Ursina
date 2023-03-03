from ursina import *
from .Experience import Experience
from .TextureMapping import TextureMapping


class GameEntity(Entity):
    def __init__(self, name: str, star_rating: int = 0, texture_mapping: TextureMapping = TextureMapping()):
        super().__init__(
            model="quad",
            texture=texture_mapping.get_idle_texture()
        )
        self.texture_mapping = texture_mapping
        self.star_rating = star_rating
        self.name = name
        self.experience = Experience()

    def add_xp(self, amount):
        self.experience.xp += amount
        while self.experience.xp >= self.experience.get_xp_required(self.star_rating):
            self.level_up()
            self.experience.xp -= self.experience.get_xp_required(self.star_rating)

    def level_up(self):
        self.experience.level += 1
        self.update_stats()

    def update_stats(self):
        pass

    @staticmethod
    def check_minimum(variable, multiplier=1, subtract_one_true=False):
        if variable < 1:
            return 1 if not subtract_one_true else 0
        else:
            return variable * multiplier