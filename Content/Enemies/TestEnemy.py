from ursina import *

from Entity.Enemy.Enemy import Enemy


class TestEnemy(Enemy):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Test Enemy"

    def update(self):
        if held_keys['o']:
            self.damage(50)
