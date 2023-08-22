from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping


class CharacterName(Character):
    def __init__(self, *args, **kwargs):
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
            ),
            *args,
            **kwargs
        )

        # stats
        self._stats.statname.points = 1

        # skills
        self.secondary = None
        self.utility = None
        self.ultimate = None

        # events

    @property
    def name(self) -> str:
        return "name"

    @property
    def star_rating(self) -> int:
        return 1
