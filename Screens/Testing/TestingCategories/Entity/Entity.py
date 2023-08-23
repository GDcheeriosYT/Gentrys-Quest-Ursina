from ...Category import Category

from .CharacterTest import CharacterTest
from .EnemyTest import EnemyTest
from .EntityPoolTest import EntityPoolTest


class Entity(Category):
    def __init__(self):
        super().__init__(
            "Entity",
            [
                CharacterTest(),
                EnemyTest(),
                EntityPoolTest()
            ]
        )
