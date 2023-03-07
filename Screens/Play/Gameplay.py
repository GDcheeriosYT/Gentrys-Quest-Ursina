from ursina import *
from Entity.Character.Character import Character
from Graphics.UIs.GameplayUI.GameplayUI import GameplayUI
from ..Screen import Screen


class GameplayScreen(Screen):
    def __init__(self, player: Character):
        self.player = player
        self.ui = GameplayUI(player)
