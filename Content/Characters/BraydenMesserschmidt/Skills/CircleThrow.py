from Entity.Character.Skill.Skill import Skill
from ursina import *


class CircleThrow(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate

    @property
    def name(self) -> str:
        return "Circle Throw"

    @property
    def description(self) -> str:
        return '''
        throw a circle that does something
        '''
    
    @property
    def cooldown(self) -> int:
        return 5

    @property
    def icon(self) -> str:
        return "Textures/Circle.png"

    def _on_activate(self):
        self._circle = Entity(
            model='quad',
            texture='Textures/Circle.png',
        )
        self.deactivate()
        invoke(self._on_deactivate, delay=2)

    def _on_deactivate(self):
        destroy(self._circle)
        self._circle = None
