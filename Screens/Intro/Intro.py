from ursina import *
from ursina.curve import *

import Game
from GameStates import GameStates
from ..Screen import Screen
import GameConfiguration


class Intro(Screen):
    def __init__(self):
        super().__init__()
        Game.audio_system.set_music("Audio/GentrysTheme.mp3", False)
        self.engine_icon = Entity(
            model="quad",
            scale=(0.25, 0.25),
            texture="Graphics/Textures/ursina_chan_alpha.png",
            alpha=0,
            parent=self
        )
        self.engine_info_container = Entity(
            aplha=0,
            parent=self
        )
        self.engine_title = Text(
            "ursina engine",
            alpha=0,
            origin=(0, 0),
            position=(0, -0.25),
            scale=(3, 3),
            parent=self.engine_info_container
        )
        self.engine_description = Text(
            "open source game engine",
            origin=(0, 0),
            alpha=0,
            position=(0, -0.35),
            scale=(2, 2),
            parent=self.engine_info_container
        )

        self.fade_delay = 0.5
        self.fade_time = 1.5

        self.on_show += self._show

    def _show(self):
        Game.audio_system.toggle_music_pause(True, 4.5)
        # invoke(lambda: self.engine_icon.fade_in(1, self.fade_time), delay=self.fade_delay)
        # invoke(lambda: self.engine_title.fade_in(1, self.fade_time), delay=self.fade_delay)
        # invoke(lambda: self.engine_description.fade_in(1, self.fade_time), delay=self.fade_delay * 4)
        # invoke(lambda: self.engine_icon.fade_in(0, self.fade_time * 4), delay=self.fade_delay * 10)
        # invoke(lambda: self.engine_title.fade_in(0, self.fade_time * 4), delay=self.fade_delay * 10)
        # invoke(lambda: self.engine_description.fade_in(0, self.fade_time * 4), delay=self.fade_delay * 12)
        invoke(lambda: Game.change_state(GameStates.mainMenu), delay=13)

    @property
    def name(self) -> str:
        return "Intro"

    @property
    def color(self) -> color:
        return color.black

    @property
    def fades(self) -> bool:
        return False
