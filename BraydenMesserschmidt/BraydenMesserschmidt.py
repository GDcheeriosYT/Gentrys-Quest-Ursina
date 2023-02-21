from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping


class BraydenMesserschmidt(Character):
    def __init__(self):
        super().__init__(
            "Brayden Messerschmidt",
            5,
            texture_mapping=TextureMapping(
                idle_textures=["Textures/body.png"]
            )
        )