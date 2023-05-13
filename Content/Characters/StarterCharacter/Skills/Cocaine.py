from Entity.Character.Skill.Skill import Skill
from ursina import *


class Cocaine(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate

    @property
    def name(self) -> str:
        return "Cocaine"

    def _on_activate(self):
        self.character.stats.speed.add_value(2)
        self.character.stats.attack_speed.add_value(0.7)
        invoke(lambda: self.character.stats.speed.remove_value(2), delay=7)
        invoke(lambda: self.character.stats.attack_speed.remove_value(0.7), delay=7)
        self.deactivate()

    @property
    def icon(self):
        return "Textures/cocaineicon.png"

    @property
    def description(self) -> str:
        return '''
        increases speed by 2 and attack speed by 0.7 
        cooldown 15 seconds
        '''

    @property
    def cooldown(self) -> int:
        return 30
