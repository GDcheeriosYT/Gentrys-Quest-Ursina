import GameConfiguration
from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from ursina import *


class MasonJames(Character):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Mason James"

    @property
    def texture_mapping(self) -> TextureMapping:
        return TextureMapping(
            idle_textures=["Textures/body.png"]
        )

    @property
    def star_rating(self) -> int:
        return 5

    @property
    def audio_mapping(self) -> AudioMapping:
        return AudioMapping(
            ["Audio/spawn.mp3"]
        )