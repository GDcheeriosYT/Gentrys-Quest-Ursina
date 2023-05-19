from Entity.Enemy.Enemy import Enemy
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from ursina import *


class EnemyName(Enemy):
    def __init__(self):
        super().__init__(
            TextureMapping(
                idle_textures=["Textures/texturename.fileformat"],
                damage_textures=["Textures/texturename.fileformat"],
                walk_textures=["Textures/texturename.fileformat"]
            ),
            AudioMapping(
                spawn_sounds=["Audio/audioname.fileformat"],
                levelup_sounds=["Audio/audioname.fileformat"],
                damage_sounds=["Audio/audioname.fileformat"],
                death_sounds=["Audio/audioname.fileformat"]
            )
        )

        # stats


    @property
    def name(self) -> str:
        return "Enemy Name"
