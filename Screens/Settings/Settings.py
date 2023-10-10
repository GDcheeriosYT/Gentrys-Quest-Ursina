from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu

import Game
import GameConfiguration
from GameStates import GameStates
from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from Graphics.GameButton import GameButton
from Graphics.GameText import GameText
from .Components.Setting import Setting
from .Components.ToggleButton import ToggleButton
from Overlays.Notification import Notification


class Settings(Screen):
    def __init__(self):
        super().__init__(True, GameStates.mainMenu)
        self.menu_text = TitleText(Game.language.settings, parent=self)
        self.menu_text.y = 0.35
        self.menu_text.disable()

        self.on_show += self._show
        self.on_hide += self._hide

        language_menu = DropdownMenu(
            Game.language.name,
            [language().get_button() for language in Game.content_manager.languages]
        )

        def assign_clicky(button):
            def clicky():
                language_menu.text_entity.text = button.text_entity.text

            button.on_click = clicky

        for button in language_menu.buttons:
            assign_clicky(button)

        language_menu.text_entity.font = Game.language.font

        self.settings = [
            # language
            Setting(Game.language.language, language_menu, parent=self),

            # audio
            GameText(Game.language.audio, origin=(0, 0), parent=self),
            Setting(Game.language.music_volume, Slider(default=GameConfiguration.music_volume, step=0.01), parent=self),
            Setting(Game.language.sound_volume, Slider(default=GameConfiguration.sound_volume, step=0.01), parent=self),

            # graphics
            GameText(Game.language.graphics, origin=(0, 0), parent=self),
            Setting(Game.language.fullscreen, ToggleButton(GameConfiguration.fullscreen, "on", "off"), parent=self),
            Setting(Game.language.extra_ui_info, ToggleButton(GameConfiguration.extra_ui_info, "on", "off"), parent=self)
        ]

        y = 0.2

        for setting in self.settings:
            setting.position = (0, y)
            y -= 0.1

        self.apply_button = GameButton(
            Game.language.apply,
            position=(0.03, -0.45),
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
                # language
                if setting.setting_text.text == Game.language.language:
                    value = setting.get_setting().text_entity.text
                    print("language", value)
                    GameConfiguration.language = value
                    Game.language = Game.content_manager.get_language(value)

                # audio
                if setting.setting_text.text == Game.language.music_volume:
                    value = setting.get_setting().value
                    GameConfiguration.music_volume = value
                    Game.audio_system.change_music_volume(value)
                elif setting.setting_text.text == Game.language.sound_volume:
                    value = setting.get_setting().value
                    GameConfiguration.sound_volume = value
                    Game.audio_system.change_sound_volume(value)

                # graphics
                elif setting.setting_text.text == Game.language.fullscreen:
                    GameConfiguration.fullscreen = setting.get_setting().toggled
                elif setting.setting_text.text == Game.language.extra_ui_info:
                    GameConfiguration.extra_ui_info = setting.get_setting().toggled

        Game.notification_manager.add_notification(Notification(Game.language.applied_settings, color.green))
        GameConfiguration.apply_settings()
        GameConfiguration.save_settings()

        Game.reload_screen()


    @property
    def name(self) -> str:
        return "Settings"
