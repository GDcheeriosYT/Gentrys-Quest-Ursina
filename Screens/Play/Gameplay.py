from Entity.Character.Character import Character
from Graphics.UIs.GameplayUI.GameplayUI import GameplayUI
from ..Screen import Screen
from ursina import *


class GameplayScreen(Screen):
    def __init__(self, player: Character):
        super().__init__()
        self.player = player
        self.ui = GameplayUI(player)
        self.player.spawn()
        self.player.on_damage += self.ui.update_data
        self.player.on_heal += self.ui.update_data
        self.ui.update_data()

    @property
    def allow_back(self) -> bool:
        return False
