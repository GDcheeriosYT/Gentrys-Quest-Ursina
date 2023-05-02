from ursina import *

import Game
from GameStates import GameStates
from User.User import User


class GuestConfirmBox(Entity):
    def __init__(self, username, *args, **kwargs):
        super().__init__(
            model=Quad(0.15),
            origin=(0, 0),
            scale=(0.6, 0.6),
            color=rgb(117, 117, 117),
            parent=camera.ui,
            *args,
            **kwargs
        )

        self._username = username

        self._confirm_text = Text(f"You want to play as {username}?", position=(0, 0.3), origin=(0, 0),
                                  scale=(2.5, 2.5), parent=self)
        self._confirm_box = Button("Confirm", position=(0, -0.2), scale=(0.2, 0.1), parent=self)
        self._confirm_box.on_click = self.on_click

    def on_click(self):
        user = User(self._username, True)
        user.replace_data(open(f"Data/{self._username}.json", "r").read())
        Game.user = user
        Game.state = GameStates.started
        destroy(self)
