from Entity.Enemy.Enemy import Enemy
from ursina import *
from Content.Weapons.Knife.Knife import Knife


class TestEnemy(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.swap_weapon(Knife())

    @property
    def name(self) -> str:
        return "Test Enemy"
