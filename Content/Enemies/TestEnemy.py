from Entity.Enemy.Enemy import Enemy
from ursina import *


class TestEnemy(Enemy):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Test Enemy"
