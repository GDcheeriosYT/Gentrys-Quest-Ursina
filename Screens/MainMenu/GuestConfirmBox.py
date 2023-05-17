from ursina import *

import Game
from GameStates import GameStates
from Content.Characters.StarterCharacter.StarterCharacter import StarterCharacter
from Content.Characters.BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Characters.PeteMarks.PeteMarks import PeteMarks
from User.User import User


class GuestConfirmBox(Entity):
    def __init__(self, username, menu, *args, **kwargs):
        super().__init__(
            model=Quad(0.15),
            origin=(0, 0),
            scale=(0.6, 0.6),
            position=(0, -0.1),
            color=color.clear,
            parent=camera.ui,
            *args,
            **kwargs
        )

        self._username = username
        self._menu = menu
        menu.disable()

        self._confirm_text = Text(f"You want to play as\n{username}?", position=(0, 0.3), origin=(0, 0),
                                  scale=(2.5, 2.5), parent=self)
        self._confirm_box = Button("Confirm", position=(0, -0.2), scale=(0.2, 0.1), parent=self)
        self._confirm_box.on_click = self.confirm_on_click
        self._back_box = Button("X", position=(0.5, 0.5), scale=(0.05, 0.05), origin=(0.5, 0.5), parent=self)
        self._back_box.on_click = self.back_on_click

    def confirm_on_click(self):
        user = User(self._username, True)
        user.replace_data(open(f"Data/{self._username}.json", "r").read())
        Game.user = user
        if user.user_data.startup_amount == 0:
            if user.username == "GDcheerios":
                starter_character = BraydenMesserschmidt()
            elif user.username == "limechips":
                starter_character = PeteMarks()
            else:
                starter_character = StarterCharacter(user.username)
            user.equip_character(starter_character)
            user.add_character(StarterCharacter(user.username))
            Game.change_state(GameStates.tutorial)
        self._menu.enable()
        destroy(self)

    def back_on_click(self):
        self._menu.enable()
        destroy(self)
