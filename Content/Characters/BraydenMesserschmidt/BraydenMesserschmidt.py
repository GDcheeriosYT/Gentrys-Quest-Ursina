from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from ursina import *


class BraydenMesserschmidt(Character):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Brayden Messerschmidt"

    @property
    def texture_mapping(self) -> TextureMapping:
        return TextureMapping(
            idle_textures=["body.png"]
        )

    @property
    def star_rating(self) -> int:
        return 5

    @property
    def audio_mapping(self) -> AudioMapping:
        return AudioMapping(
            spawn_sounds=["Audio/spawn.mp3"],
            damage_sounds=["Audio/damage.mp3"]
        )