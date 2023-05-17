from Entity.Character.Skill.Skill import Skill
from ursina import *


class FourEightFourOneFour(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate

    '''
    WIP
    '''

    @property
    def name(self) -> str:
        return "Four Eight Four One Four"

    @property
    def description(self) -> str:
        return '''
        Pulls nearby enemies in
        Cooldown 30 seconds
        '''

    @property
    def cooldown(self) -> int:
        return 30

    def _on_activate(self):
        self.deactivate()
