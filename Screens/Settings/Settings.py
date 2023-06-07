from ursina import *

import GameConfiguration
from GameStates import GameStates
from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from .Components.Setting import Setting
from .Components.ToggleButton import ToggleButton


class Settings(Screen):
    def __init__(self):
        super().__init__(True, GameStates.mainMenu)
        self.menu_text = TitleText("Settings")
        self.menu_text.y = 0.35
        self.menu_text.disable()

        self.on_show += self._show
        self.on_hide += self._hide

        self.settings = [
            # audio
            Text("Audio", parent=self),
            Setting("volume", Slider(default=GameConfiguration.volume), parent=self),

            # graphics
            Text("graphics", parent=self),
            Setting("fps", ToggleButton(GameConfiguration.hide_fps, "hidden", "shown"), parent=self),
            Setting("fullscreen", ToggleButton(GameConfiguration.fullscreen, "on", "off"), parent=self),
            Setting("extra ui info", ToggleButton(GameConfiguration.extra_ui_info, "on", "off"), parent=self)
        ]

        y = 0.2

        for setting in self.settings:
            setting.position = (0, y)
            y -= 0.1



    def _show(self):
        self.menu_text.enable()
        for setting in self.settings:
            setting.enable()

    def _hide(self):
        self.menu_text.disable()
        for setting in self.settings:
            setting.disable()

    @property
    def color(self) -> color:
        return rgb(117, 117, 117)

    @property
    def name(self) -> str:
        return "Settings"
