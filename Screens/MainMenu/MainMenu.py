from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText
from .LoginBox import LoginBox


from ursina import *


class MainMenu(Screen):
    def __init__(self, version: str):
        super().__init__()
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
        self.play_button.disable()
        self.title.disable()
        LoginBox()
