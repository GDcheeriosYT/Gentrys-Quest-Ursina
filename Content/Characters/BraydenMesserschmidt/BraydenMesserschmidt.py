from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping


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