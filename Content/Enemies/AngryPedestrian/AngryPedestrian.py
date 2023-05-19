from Entity.Enemy.Enemy import Enemy
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from Content.Weapons.Knife.Knife import Knife
from ursina import *


class AngryPedestrian(Enemy):
    def __init__(self):
        super().__init__()
        self.swap_weapon(Knife())

    @property
    def name(self) -> str:
        return "Angry Pedestrian"
