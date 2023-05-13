from Entity.Character.Character import Character
from Entity.Character.Skill.Skill import Skill
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from .Skills.CircleThrow import CircleThrow


class BraydenMesserschmidt(Character):
    def __init__(self):
        super().__init__()
        self._stats.speed.points = 1
        self._stats.crit_rate.points = 2
        self._stats.attack_speed.points = 1

        self.on_spawn += self.check_weapon

    @property
    def name(self) -> str:
        return "Brayden Messerschmidt"

    @property
    def texture_mapping(self) -> TextureMapping:
        return TextureMapping(
            idle_textures=["Content/Characters/BraydenMesserschmidt/Textures/body.png"]
        )

    @property
    def star_rating(self) -> int:
        return 5

    @property
    def secondary(self) -> Skill:
        return CircleThrow()

    @property
    def utility(self) -> Skill:
        return CircleThrow()

    @property
    def ultimate(self) -> Skill:
        return CircleThrow()

    def check_weapon(self):
        if self.weapon.name == "Braydens Osu Pen":
            self.stats.boost_all_stats(10)

    @property
    def audio_mapping(self) -> AudioMapping:
        return AudioMapping(
            spawn_sounds=["Audio/spawn.mp3"],
            damage_sounds=["Audio/damage.mp3"]
        )