from ursina import *
import Game
import GameConfiguration
from .MainMenu.MainMenu import MainMenu
from .Intro.Intro import Intro
from .Tutorial.Tutorial import Tutorial
from Graphics.FadeScreen import FadeScreen


class ScreenManager(Entity):
    def __init__(self):
        super().__init__()

        self.intro = Intro()
        self.main_menu = MainMenu()
        self.tutorial = Tutorial()

        self.current_screen = 0

        self.screens = [
            self.intro,
            self.main_menu,
            self.tutorial
        ]

    def transition(self):
        fade_screen = FadeScreen()
        fade_screen.fade_in(1, GameConfiguration.fade_time)
        for i in range(len(self.screens)):
            if i != self.current_screen and self.screens[i].visible:
                self.screens[i].hide()

        fade_screen.fade_out(0, GameConfiguration.fade_time * 2)
        destroy(fade_screen, GameConfiguration.fade_time ** 2)

    def change_screen(self, screen_index: int):
        self.current_screen = screen_index
        if self.current_screen != 0:
            self.transition()

        self.screens[screen_index].show()
        Game.state_affected = False

    def update(self):
        if not Game.state_affected:
            self.change_screen(Game.state.value)
            Game.state_affected = True
