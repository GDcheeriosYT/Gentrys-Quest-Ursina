import GameConfiguration
from Entity.Character.Skill.Skill import Skill
from ursina import *


class Dash(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate
        self.on_activate += lambda: Audio("Audio/Utility.m4a", volume=GameConfiguration.volume)

    @property
    def name(self) -> str:
        return "Dash"

    @property
    def description(self) -> str:
        return """
        Dashes in the direction that the player is moving
        cooldown 4 seconds
        """

    @property
    def cooldown(self) -> int:
        return 4

    def _on_activate(self):
        self.deactivate()
        self.character.position += (self.character.direction * self.character.stats.speed.get_value())
