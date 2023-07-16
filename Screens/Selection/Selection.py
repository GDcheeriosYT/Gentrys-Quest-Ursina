from ursina import *

import Game
from ..Screen import Screen
from GameStates import GameStates
from Graphics.Container import Container

from .SelectionStatus import SelectionStatus
from .MenuButton import MenuButton
from .Changelog import ChangelogMenu


class Selection(Screen):
    def __init__(self):
        self.status = SelectionStatus.changelog
        self.status_changed = True
        super().__init__(True, GameStates.mainMenu)
        self.back_button.events += self.back_thing

        self.menu = Container(
            model='quad',
            origin=(0, 0),
            scale=(1.5, 0.7),
            position=window.center,
            color=color.clear
        )

        self.menu_buttons_container = Container(
            position=(0, 0.5),
            scale=(1, 0.2),
            parent=self.menu
        )

        self.changelog = ChangelogMenu(self.menu)

        self.changelog_button = MenuButton(
            "Changelog",
            parent=self.menu_buttons_container
        )

        self.changelog_button.activate()

        self.changelog_button.on_click_event += lambda: self.change_status(SelectionStatus.changelog)

        self.travel_button = MenuButton(
            "Travel",
            parent=self.menu_buttons_container
        )

        self.travel_button.on_click_event += lambda: self.change_status(SelectionStatus.travel)

        self.menu_buttons = [
            self.changelog_button,
            self.travel_button
        ]

        space_coefficient = 1
        scale_x = 1 / (space_coefficient * len(self.menu_buttons))
        center_offset = (len(self.menu_buttons) - 1) * scale_x / 2
        for button in self.menu_buttons:
            index = self.menu_buttons.index(button)
            button.scale = (scale_x - (scale_x * 0.1), 0.5)
            button.text_entity.scale = (button, 1)
            button.position = ((index * scale_x) - center_offset, 0.35)
            print("scale", str(button.scale))
            print("position", str(button.position))

        self.on_show += self._show
        self.on_hide += self._hide

    def deactivate_buttons(self):
        for button in self.menu_buttons:
            button.deactivate()

    def _show(self):
        for button in self.menu_buttons:
            button.enable()

    def _hide(self):
        self.changelog.disable()
        for button in self.menu_buttons:
            button.disable()

    def change_status(self, status: SelectionStatus):
        self.status = status
        self.status_changed = True

    def back_thing(self):
        Game.user.unload()

    def update(self):
        if self.status_changed:
            self.deactivate_buttons()
            if self.status == SelectionStatus.changelog:
                self.changelog_button.activate()
                self.changelog.enable()

            elif self.status == SelectionStatus.travel:
                self.changelog.disable()
                self.travel_button.activate()

            self.status_changed = False
