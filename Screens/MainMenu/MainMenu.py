# game packages
# graphics packages
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText

# external packages
from ursina import *


class MainMenu:
    def __init__(self, version: str):
        self.title = TitleText("Gentry's Quest", hidden=True)
        self.version = VersionText(version)
        self.play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
        self.title.fade_in(1, 2)
        self.audio = Audio("Audio/song.mp3", volume=0.1)
        self.audio.fade_in(0.1, 2)
