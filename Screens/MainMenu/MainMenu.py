import GameConfiguration
from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText
from Graphics.FadeScreen import FadeScreen
from Graphics.Buttons.TabButton import TabButton
from .LoginUI import LoginUI
from .GuestUI import GuestUI
from GameStates import GameStates

from Graphics.GameButton import GameButton

import Game

from ursina import *

already_updated = False


def _guest_click():
    global already_updated
    MainMenu.is_guest_menu = True
    MainMenu.is_login_menu = False
    already_updated = False


def _login_click():
    global already_updated
    MainMenu.is_login_menu = True
    MainMenu.is_guest_menu = False
    already_updated = False


class MainMenu(Screen):
    is_guest_menu = False
    is_login_menu = True

    def __init__(self):
        super().__init__()
        self.version = VersionText(Game.version)
        self.title = TitleText("Gentry's Quest", color=color.black)
        self.play_button = GameButton(Game.language.play, position=(0, -0.1), scale=(0.2, 0.05))
        self.settings_button = GameButton(Game.language.settings, position=(0, -0.3), scale=(0.2, 0.05))
        self.guest_button = TabButton(Game.language.guest, position=(-0.17, 0.45, 0))
        self.guest_button.on_click = _guest_click
        self.login_button = TabButton(Game.language.login, position=(0.17, 0.45, 0))
        self.login_button.on_click = _login_click
        self.menu = Entity(model=Quad(0.05), color=rgb(117, 117, 117), position=(0, -0.065), scale=(0.74, 0.74),
                           parent=camera.ui)
        self.in_menu = False
        self.menu.disable()
        self.guest_screen = GuestUI()
        self.login_screen = LoginUI()
        self.guest_button.disable()
        self.login_button.disable()
        self.title.disable()
        self.play_button.disable()
        self.settings_button.disable()
        self.settings_button.on_click = lambda: Game.change_state(GameStates.settings)
        self.version.disable()
        self.play_button.on_click = self.play

        self.on_show += self._show
        self.on_hide += self._hide

    @property
    def name(self) -> str:
        return "Main Menu"

    @property
    def fades(self) -> bool:
        return False

    def on_show(self) -> None:
        self.title.fade_in(1, 1)
        self.play_button.fade_in(1, 1)
        self.settings_button.fade_out(0, 0.5)

    def on_hide(self) -> None:
        self.title.fade_out(0, 0.5)
        self.play_button.fade_out(0, 0.5)
        self.settings_button.fade_out(0, 0.5)

    def menu_toggle(self) -> None:
        self.in_menu = not self.in_menu

    def _show(self):
        global already_updated
        self.title.enable()
        self.version.enable()
        self.play_button.enable()
        self.settings_button.enable()
        MainMenu.is_guest_menu = False
        MainMenu.is_login_menu = True
        already_updated = False

    def _hide(self):
        self.login_screen.disable()
        self.guest_screen.disable()
        self.menu.disable()
        self.version.disable()
        self.guest_button.disable()
        self.login_button.disable()
        self.title.disable()
        self.play_button.disable()
        self.settings_button.disable()
        self.in_menu = False

    def play(self) -> None:
        fade_screen = FadeScreen()
        fade_screen.fade_in(1, GameConfiguration.fade_time)
        Game.audio_system.fade_music("Audio/Gentrys_Quest_Ambient_1.mp3", GameConfiguration.fade_time * 2)
        invoke(lambda: self.play_button.disable(), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: self.settings_button.disable(), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: self.title.disable(), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: self.guest_button.enable(), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: self.login_button.enable(), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: self.menu.enable(), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: fade_screen.fade_out(0, GameConfiguration.fade_time), delay=GameConfiguration.fade_time * 2)
        invoke(lambda: self.menu_toggle(), delay=GameConfiguration.fade_time * 2)
        destroy(fade_screen, GameConfiguration.fade_time * 5)

    def input(self, key):
        if key == 'p':
            self.guest_screen.update_list()

    def update(self):
        global already_updated
        if self.in_menu:
            if MainMenu.is_guest_menu and not already_updated:
                self.guest_screen.update_list()
                self.guest_button.color = rgb(117, 117, 117)
                self.login_button.color = rgb(0, 0, 0)
                self.guest_screen.enable()
                self.login_screen.disable()
                already_updated = True

            elif MainMenu.is_login_menu and not already_updated:
                self.guest_button.color = rgb(0, 0, 0)
                self.login_button.color = rgb(117, 117, 117)
                self.guest_screen.disable()
                self.login_screen.enable()
                already_updated = True
