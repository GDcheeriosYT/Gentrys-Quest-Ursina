from ursina import *
from .Experience import Experience
from .TextureMapping import TextureMapping
from utils.Event import Event


class GameEntityBase(Entity):
    def __init__(self):
        super().__init__(
            model="quad",
            texture="huh.png"
        )

    @property
    def name(self) -> str:

        '''
        The name of the GameEntity
        '''

        raise NotImplementedError

    @property
    def experience(self) -> Experience:
        '''
        The experience of the GameEntity
        '''
        return Experience()

    def add_xp(self, amount):
        self.experience.xp += amount
        while self.experience.xp >= self.experience.get_xp_required(self.star_rating):
            self.level_up()
            self.experience.xp -= self.experience.get_xp_required(self.star_rating)

        self.on_add_xp()

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

    @property
    def on_level_up(self) -> Event:
        return Event("OnLevelUp", 0)

    @property
    def on_add_xp(self) -> Event:
        return Event("OnAddXp", 0)