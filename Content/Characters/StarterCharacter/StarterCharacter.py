from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping


class StarterCharacter(Character):
    def __init__(self, name: str):
        super().__init__(TextureMapping(idle_textures=["Textures/body.png"]))
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def star_rating(self) -> int:
        return 1
