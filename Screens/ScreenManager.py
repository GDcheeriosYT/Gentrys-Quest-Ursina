from ursina import *
import Game
import GameConfiguration
from .MainMenu.MainMenu import MainMenu
from .Intro.Intro import Intro
from .Testing.Testing import Testing
from .Tutorial.Tutorial import Tutorial
from .Settings.Settings import Settings
from .Gameplay.Gameplay import Gameplay
from .Selection.Selection import Selection
from Graphics.FadeScreen import FadeScreen
from Graphics.Overlays.DebugOverlay import DebugOverlay


class ScreenManager(Entity):
    def __init__(self, app):
        super().__init__()

        self.transitions = 0

        self._app = app

        self.debug_overlay = DebugOverlay()
        self.debug_overlay.disable()

        self.screens = []

        self.assign_screen(Intro)
        self.assign_screen(MainMenu)
        self.assign_screen(Tutorial)
        self.assign_screen(Settings)
        self.assign_screen(Gameplay)
        self.assign_screen(Selection)
        self.assign_screen(Testing)

        self.current_screen = None

    def transition(self, fade: bool):
        self.transitions += 1
        if fade:
            fade_screen = FadeScreen()
            fade_screen.fade_in(1, GameConfiguration.fade_time)
            invoke(lambda: self.screen_disable_sequence(), delay=GameConfiguration.fade_time)
            invoke(lambda: self._app.setBackgroundColor(self.screens[self.current_screen].color), delay=GameConfiguration.fade_time)
            invoke(lambda: fade_screen.fade_out(0, GameConfiguration.fade_time * 2), delay=GameConfiguration.fade_time * 2.1)
            destroy(fade_screen, 5)
        else:
            self.screen_disable_sequence()
            self._app.setBackgroundColor(self.screens[self.current_screen].color)

    def change_screen(self, screen_index: int):
        self.current_screen = screen_index
        self.transition(fade=True) if self.screens[self.current_screen].fades else self.transition(fade=False)
        invoke(self.screens[screen_index].show, delay=GameConfiguration.fade_time if self.screens[self.current_screen].fades else 0)
        Game.state_affected = False

    def screen_disable_sequence(self):
        for i in range(len(self.screens)):
            if i != self.current_screen and self.screens[i].visible:
                self.screens[i].hide()

    def assign_screen(self, screen):
        screen = screen()
        screen.hide()
        self.screens.append(screen)

    def update(self):
        if not Game.state_affected:
            self.change_screen(Game.state.value)
            Game.state_affected = True

    def kill(self):
        fade_screen = FadeScreen()
        fade_screen.alpha = 0

        fade_screen.fade_in(1, GameConfiguration.fade_time)
        [destroy(screen, GameConfiguration.fade_time) for screen in self.screens]
        destroy(self, GameConfiguration.fade_time*1.1)
        invoke(lambda: fade_screen.fade_out(0, GameConfiguration.fade_time), delay=GameConfiguration.fade_time*2)
        destroy(fade_screen, GameConfiguration.fade_time * 5)

    def input(self, key):
        if key == "b":
            if self.debug_overlay.enabled:
                self.debug_overlay.disable()
            else:
                self.debug_overlay.enable()

        if key == "f2":
            GameConfiguration.save_settings()
