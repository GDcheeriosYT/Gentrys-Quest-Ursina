from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead


class Enemy(GameUnit):

    @property
    def overhead(self) -> EntityOverhead:
        return EntityOverhead(self.name, self.stats.health.get_value())
