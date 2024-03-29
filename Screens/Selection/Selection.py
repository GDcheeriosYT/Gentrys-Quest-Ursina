from ursina import *

import Game
from ..Screen import Screen
from GameStates import GameStates
from Graphics.Container import Container
from Graphics.UIs.Inventory.Inventory import Inventory
from Overlays.Notification import Notification

from .SelectionStatus import SelectionStatus
from .MenuButton import MenuButton
from .Changelog import ChangelogMenu
from .TravelMenu import TravelMenu
from .GachaMenu import GachaMenu


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

        self.changelog_menu = ChangelogMenu(self.menu)

        self.travel_menu = TravelMenu(self.menu)

        self.inventory_menu = Inventory(True, self.menu)
        self.inventory_menu.scale = (0.805, 0.85)
        self.inventory_menu.y -= 0.05

        self.gacha_menu = GachaMenu(self.menu)

        self.changelog_button = MenuButton(
            Game.language.changelog,
            parent=self.menu_buttons_container
        )

        self.changelog_button.activate()

        self.changelog_button.on_click_event += lambda: self.change_status(SelectionStatus.changelog)

        self.travel_button = MenuButton(
            Game.language.travel,
            parent=self.menu_buttons_container
        )

        def check_equipped_character():
            if Game.user.get_equipped_character() is not None:
                self.change_status(SelectionStatus.travel)
            else:
                Game.notification_manager.add_notification(Notification("You don't have anyone equipped!", color.red))

        self.travel_button.on_click_event += check_equipped_character

        self.inventory_button = MenuButton(
            Game.language.inventory,
            parent=self.menu_buttons_container
        )

        self.inventory_button.on_click_event += lambda: self.change_status(SelectionStatus.inventory)

        self.gacha_button = MenuButton(
            Game.language.gacha,
            parent=self.menu_buttons_container
        )

        self.gacha_button.on_click_event += lambda: self.change_status(SelectionStatus.gacha)

        self.menus = [
            self.changelog_menu,
            self.travel_menu,
            self.inventory_menu,
            self.gacha_menu
        ]

        self.menu_buttons = [
            self.changelog_button,
            self.travel_button,
            self.inventory_button,
            self.gacha_button
        ]

        space_coefficient = 1
        scale_x = 1 / (space_coefficient * len(self.menu_buttons))
        center_offset = (len(self.menu_buttons) - 1) * scale_x / 2
        for button in self.menu_buttons:
            index = self.menu_buttons.index(button)
            button.scale = (scale_x - (scale_x * 0.1), 0.5)
            button.text_entity.scale = (button, 1)
            button.position = ((index * scale_x) - center_offset, 0.35)

        self.on_show += self._show
        self.on_hide += self._hide

    @property
    def name(self) -> str:
        return "Selection"

    @property
    def fades(self) -> bool:
        return True

    def deactivate_buttons(self):
        for button in self.menu_buttons:
            button.deactivate()

    def disable_menus(self):
        for menu in self.menus:
            menu.disable()

    def _show(self):
        self.inventory_menu.update_player()
        self.change_status(SelectionStatus.changelog)
        self.menu.enable()
        self.menu_buttons_container.enable()

    def _hide(self):
        self.menu.disable()
        self.menu_buttons_container.disable()
        self.disable_menus()
        self.inventory_menu.show_entity_listing('characters')

    def change_status(self, status: SelectionStatus):
        self.status = status
        self.status_changed = True

    def back_thing(self):
        Game.user.unload()

    def update(self):
        if self.status_changed:
            self.deactivate_buttons()
            self.disable_menus()
            if self.status == SelectionStatus.changelog:
                self.changelog_button.activate()
                self.changelog_menu.enable()

            elif self.status == SelectionStatus.travel:
                self.travel_button.activate()
                self.travel_menu.enable()

            elif self.status == SelectionStatus.inventory:
                self.inventory_button.activate()
                self.inventory_menu.enable()

            elif self.status == SelectionStatus.gacha:
                self.gacha_button.activate()
                self.gacha_menu.enable()

            self.status_changed = False
