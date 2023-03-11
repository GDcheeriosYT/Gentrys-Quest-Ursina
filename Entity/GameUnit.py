from .GameEntityBase import GameEntityBase
from .Experience import Experience
from .Stats import Stats
from .TextureMapping import TextureMapping


class GameUnit(GameEntityBase):

    @property
    def difficulty(self) -> int:
        return 1

    @difficulty.setter
    def difficulty(self, value) -> None:
        self.difficulty = value

    @property
    def stats(self) -> Stats:
        return Stats()

    @property
    def texture_mapping(self) -> TextureMapping:
        return TextureMapping()

    def damage(self, amount):
        self.stats.health.current_value -= amount

    def heal(self, amount):
        self.stats.health.current_value += amount

    # events

    @staticmethod
    def on_heal(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def on_move(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def on_damage(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def on_death(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
