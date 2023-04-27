from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText
from Graphics.FadeScreen import FadeScreen
import GameConfiguration
from .LoginBox import LoginBox


from ursina import *


class MainMenu(Screen):
    def __init__(self, version: str, intro_music: Audio):
        super().__init__()
        self.intro_music = intro_music
        self.title = TitleText("Gentry's Quest")
        self.version = VersionText(version)
        self.play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
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

    def play(self) -> None:
        time = 0.5
        self.intro_music.fade_out(0, time)
        invoke(lambda: self.intro_music.disable(), delay=time)
        fade_screen = FadeScreen()
        fade_screen.fade_in(1, time)
        invoke(lambda: self.play_button.disable(), delay=time)
        invoke(lambda: self.title.disable(), delay=time)
        invoke(lambda: LoginBox(), delay=time)
        ambient_1 = Audio("Audio/Gentrys_Quest_Ambient_1.mp3", volume=0, loop=True)
        invoke(lambda: ambient_1.fade_in(1, time), delay=time * 2)
        invoke(lambda: fade_screen.fade_out(0, time), delay=time * 2)

