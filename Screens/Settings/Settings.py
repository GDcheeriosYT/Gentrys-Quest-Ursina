from ursina import *

import Game
import GameConfiguration
from GameStates import GameStates
from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from .Components.Setting import Setting
from .Components.ToggleButton import ToggleButton
from Overlays.Notification import Notification


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

        self.apply_button = Button(
            "apply",
            position=(0.03, -0.4),
            scale=(0.1, 0.05),
            parent=self
        )
        self.apply_button.on_click = self.apply_settings
        self.apply_button.disable()

    def _show(self):
        self.menu_text.enable()
        self.apply_button.enable()
        for setting in self.settings:
            setting.enable()

    def _hide(self):
        self.menu_text.disable()
        self.apply_button.disable()
        for setting in self.settings:
            setting.disable()

    @property
    def color(self) -> color:
        return rgb(117, 117, 117)

    @property
    def fades(self) -> bool:
        return False

    def apply_settings(self):
        for setting in self.settings:
            if isinstance(setting, Setting):
                print(setting.setting_text.text, setting.second_entity)
                # audio
                if setting.setting_text.text == "volume":
                    GameConfiguration.volume = setting.get_setting().value

                # graphics
                elif setting.setting_text.text == "fps":
                    GameConfiguration.hide_fps = setting.get_setting().toggled
                elif setting.setting_text.text == "fullscreen":
                    GameConfiguration.fullscreen = setting.get_setting().toggled
                elif setting.setting_text.text == "extra ui info":
                    GameConfiguration.extra_ui_info = setting.get_setting().toggled

        Game.notification_manager.add_notification(Notification("Applied settings", color.green))
        GameConfiguration.apply_settings()


    @property
    def name(self) -> str:
        return "Settings"
