from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping


class PhilipMcClure(Character):
    def __init__(self):
        super().__init__(
            TextureMapping(
                idle_textures=["Textures/philip.png"]
            ),
            AudioMapping(
                spawn_sounds=["Audio/spawn.m4a"],
                levelup_sounds=["Audio/levelup.m4a"],
                damage_sounds=["Audio/damage.m4a"],
                death_sounds=["Audio/death.m4a"]
            )
        )

        # stats
        self._stats.speed.points = 2
        self._stats.attack_speed.points = 2

        # skills
        self.secondary = None
        self.utility = None
        self.ultimate = None

        # events

    @property
    def name(self) -> str:
        return "Philip McClure"

    @property
    def star_rating(self) -> int:
        return 5
