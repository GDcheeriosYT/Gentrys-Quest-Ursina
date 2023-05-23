from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from .Skills.TheSecondBoofHit import TheSecondBoofHit
from .Skills.Cocaine import Cocaine
from .Skills.BrutalOverdose import BrutalOverdose


class StarterCharacter(Character):
    def __init__(self, name: str):
        super().__init__(
            TextureMapping(
                idle_textures=["Textures/body2.png"]  # add body.png and body1.png when path issue is figured out
            ),
            AudioMapping(
                spawn_sounds=[f"Audio/spawn.m4a"]
            )
        )
        self._name = name
        self.secondary = TheSecondBoofHit()
        self.utility = Cocaine()
        self.ultimate = BrutalOverdose()

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return "The Guy!"

    @property
    def star_rating(self) -> int:
        return 1
