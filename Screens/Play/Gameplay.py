from Entity.Character.Character import Character
from Graphics.UIs.GameplayUI.GameplayUI import GameplayUI
from ..Screen import Screen


class GameplayScreen(Screen):
    def __init__(self, player: Character):
        super().__init__()
        self.player = player
        self.ui = GameplayUI(player)

    def update(self):
        self.ui.update_data()
