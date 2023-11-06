from ursina import *

import Game

from Entity.Character.Skill.Skill import Skill


class CircleThrow(Skill):
    def __init__(self):
        super().__init__()
        self._sound = Audio("Audio/Secondary.m4a", autoplay=False)

        self.on_activate += self._on_activate
        self.on_activate += lambda: Game.audio_system.play_sound(self._sound)

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
            model='circle',
            collider='sphere',
            position=self.character.position,
            texture='Textures/Circle.png',
        )
        mouse_pos = mouse.position
        new_pos = self._circle.position + mouse_pos
        print(new_pos)
        self._circle.animate_position(new_pos, duration=2, curve=curve.linear)

        self.deactivate()
        invoke(self._on_deactivate, delay=2)

    def _on_deactivate(self):
        destroy(self._circle)
        self._circle = None
