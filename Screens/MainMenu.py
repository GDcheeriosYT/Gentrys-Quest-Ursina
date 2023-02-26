# game packages
# graphics packages
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText

# external packages
from ursina import *


class MainMenu:
    def __init__(self, version: str):
        self.title = TitleText("Gentry's Quest")
        self.version = VersionText(version)
        self.play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
