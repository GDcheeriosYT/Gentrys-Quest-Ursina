from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping


class StarterCharacter(Character):
    def __init__(self, name: str):
        string_path = "Content/Characters/StarterCharacter/Textures/"
        super().__init__(TextureMapping(idle_textures=[f"{string_path}body.png", f"{string_path}body1.png", f"{string_path}body2.png"]))
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def star_rating(self) -> int:
        return 1
