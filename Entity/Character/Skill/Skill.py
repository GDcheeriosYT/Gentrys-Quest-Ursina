from typing import Union
from ursina import *

import Game
from utils.Event import Event


class Skill:
    def __init__(self):
        self.on_activate = Event('OnActivate', 0)
        self.on_deactivate = Event('OnDeactivate', 0)
        self._time_started = 0
        self.activated = False
        self.is_ready = True
        self.percentage = 1

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def description(self) -> str:
        raise NotImplementedError

    @property
    def icon(self) -> str:
        return "Entity/Textures/huh.png"

    @property
    def cooldown(self) -> Union[int, float]:
        raise NotImplementedError

    @property
    def character(self):
        return Game.user.get_equipped_character()

    def activate(self):
        self.activated = True
        self.on_activate()

    def deactivate(self):
        self.activated = False
        self.is_ready = False
        self._time_started = time.time()
        self.on_deactivate()

    def update_time(self):
        time_elapsed = time.time() - self._time_started
        self.percentage = round(time_elapsed / self.cooldown, 2)

        if self.percentage >= 1:
            self.is_ready = True
