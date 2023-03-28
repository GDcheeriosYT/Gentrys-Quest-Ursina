from Entity.Character.Character import Character
from Graphics.UIs.GameplayUI.GameplayUI import GameplayUI
from ..Screen import Screen


class GameplayScreen(Screen):
    def __init__(self, player: Character):
        super().__init__()
        self.player = player
        self.ui = GameplayUI(player)
        self.ui.update_data()

    @property
    def allow_back(self) -> bool:
        return False

    def update(self):
        #self.ui.update_data()
        pass
