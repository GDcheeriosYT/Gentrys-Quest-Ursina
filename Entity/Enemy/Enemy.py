from ursina import *
from ..GameEntity import GameEntity
from ..Stats import Stats
from ursina.prefabs.health_bar import HealthBar
from typing import Union


class Enemy(GameEntity):
    def __init__(self, name: str):
        super().__init__(
            name,
            1
        )

        self.stats = Stats()
        self.health = self.stats.health.get_value()
        self.health_bar = HealthBar(max_value=self.stats.health.get_value())

