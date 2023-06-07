from Entity.Enemy.Enemy import Enemy
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from Content.Weapons.Knife.Knife import Knife
from ursina import *


class AngryPedestrian(Enemy):
    def __init__(self):
        super().__init__(
            texture_mapping=TextureMapping(
                idle_textures=["Textures/Angrybody.jpeg"]
            )
        )
        self.swap_weapon(Knife())

        # stats
        self.stats.attack.points = 7
        self.stats.health.points = 9

    @property
    def name(self) -> str:
        return "Angry Pedestrian"
