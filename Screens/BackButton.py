from ursina import *

import Game
from GameStates import GameStates
from utils.Event import Event


class BackButton(Button):
    def __init__(self, game_state: GameStates):
        super().__init__(
            "back",
            position=(-0.75, -0.4),
            scale=(0.2, 0.05),
            parent=camera.ui
        )
        self.back_to_state = game_state
        self.events = Event('events', 0)

    def on_click(self):
        self.events()
        Game.change_state(self.back_to_state)
