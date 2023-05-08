from ..Screen import Screen
from Graphics.UIs.HUD.HUD import HUD
import Game


class Tutorial(Screen):
    def __init__(self):
        super().__init__()
        self.on_show += self._show

    def _show(self):
        self.player = Game.user.get_equipped_character()
        self.player.spawn()
        self.hud = HUD(self.player)

    @property
    def name(self) -> str:
        return "Tutorial"

    @property
    def fades(self) -> bool:
        return True
