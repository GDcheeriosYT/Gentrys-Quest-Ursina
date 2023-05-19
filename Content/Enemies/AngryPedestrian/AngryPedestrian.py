from Entity.Enemy.Enemy import Enemy
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from Content.Weapons.Knife.Knife import Knife
from ursina import *


class AngryPedestrian(Enemy):
    def __init__(self):
        super().__init__()
        self.swap_weapon(Knife())

        # stats
        self.stats.attack.points = 57
        self.stats.health.points = 900
        self.experience.level = 20

    @property
    def name(self) -> str:
        return "Angry Pedestrian"
