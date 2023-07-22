from Entity.Enemy.Enemy import Enemy
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from ursina import *


class AngryChineseMan(Enemy):
    def __init__(self):
        super().__init__(
            TextureMapping(
                idle_textures=["Textures/angrychinesebody.gif"]
            ),
            AudioMapping(
                spawn_sounds=["Audio/chinesespawn.m4a"]
            )
        )

        # stats
        self.stats.attack_speed.points = 2
        self.stats.speed.points = 5

    @property
    def name(self) -> str:
        return "Angry Chinese Man"
