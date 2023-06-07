from ursina import *

import Game
from GameStates import GameStates


class BackButton(Button):
    def __init__(self, game_state: GameStates):
        super().__init__(
            "back",
            position=(-0.5, -0.4),
            scale=(0.2, 0.05),
            parent=camera.ui
        )
        self.back_to_state = game_state

    def on_click(self):
        Game.change_state(self.back_to_state)
