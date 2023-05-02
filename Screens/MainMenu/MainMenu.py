import GameConfiguration
from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText
from Graphics.FadeScreen import FadeScreen
from Graphics.Buttons.TabButton import TabButton
from .LoginUI import LoginUI
from .GuestUI import GuestUI
from utils.BooleanMethods import switch

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
    is_guest_menu = True
    is_login_menu = False

    def __init__(self, version: str, intro_music: Audio):
        super().__init__()
        self.intro_music = intro_music
        self.version = VersionText(version)
        self.title = TitleText("Gentry's Quest")
        self.play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
        self.guest_button = TabButton("Guest", position=(-0.17, 0.45, 0))
        self.guest_button.on_click = _guest_click
        self.login_button = TabButton("Login", position=(0.17, 0.45, 0))
        self.login_button.on_click = _login_click
        self.menu = Entity(model=Quad(0.05), color=rgb(117, 117, 117), position=(0, -0.065), scale=(0.74, 0.74),
                           parent=camera.ui)
        self.in_menu = False
        self.menu.disable()
        self.screen = Entity()
        self.screen.disable()
        self.guest_button.disable()
        self.login_button.disable()
        self.play_button.on_click = self.play
        self.show()

    @property
    def name(self) -> str:
        return "Main Menu"

    @property
    def allow_back(self) -> bool:
        return False

    def on_show(self) -> None:
        self.title.fade_in(1, 1)

    def on_hide(self) -> None:
        self.title.fade_out(0, 0.5)
        self.play_button.fade_out(0, 0.5)

    def menu_toggle(self) -> None:
        self.in_menu = not self.in_menu

    def play(self) -> None:
        time = 0.6
        self.intro_music.fade_out(0, time)
        invoke(lambda: self.intro_music.disable(), delay=time)
        fade_screen = FadeScreen()
        fade_screen.fade_in(1, time)
        invoke(lambda: self.play_button.disable(), delay=time * 2)
        invoke(lambda: self.title.disable(), delay=time * 2)
        invoke(lambda: self.guest_button.enable(), delay=time * 2)
        invoke(lambda: self.login_button.enable(), delay=time * 2)
        invoke(lambda: self.menu.enable(), delay=time * 2)
        invoke(lambda: self.screen.enable(), delay=time * 2)
        ambient_1 = Audio("Audio/Gentrys_Quest_Ambient_1.mp3", volume=0, loop=True)
        invoke(lambda: ambient_1.fade_in(GameConfiguration.volume, time), delay=time * 2)
        invoke(lambda: fade_screen.fade_out(0, time), delay=time * 2)
        invoke(lambda: self.menu_toggle(), delay=time * 2)

    def update(self):
        global already_updated
        if self.in_menu:
            if MainMenu.is_guest_menu and not already_updated:
                self.guest_button.color = rgb(117, 117, 117)
                self.login_button.color = rgb(0, 0, 0)
                destroy(self.screen)
                self.screen = GuestUI()
                already_updated = True

            elif MainMenu.is_login_menu and not already_updated:
                self.guest_button.color = rgb(0, 0, 0)
                self.login_button.color = rgb(117, 117, 117)
                destroy(self.screen)
                self.screen = LoginUI()
                already_updated = True
