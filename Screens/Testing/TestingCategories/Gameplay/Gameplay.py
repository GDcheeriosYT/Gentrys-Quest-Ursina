from ...Category import Category

from .FightTest import FightTest
from .GameplayTest import GameplayTest


class Gameplay(Category):
    def __init__(self):
        super().__init__(
            "Gameplay",
            [
                FightTest(),
                GameplayTest()
            ]
        )
