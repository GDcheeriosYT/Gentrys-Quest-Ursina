from ursina import *
from ..Screen import Screen
from Graphics.UIs.HUD.HUD import HUD
import Game
from .Map.TutorialMap import TutorialMap
from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen

class Tutorial(Screen):
    def __init__(self):
        super().__init__()
        self.on_show += self._show

    def _show(self):
        self.player = Game.user.get_equipped_character()
        self.player.swap_weapon(BraydensOsuPen())
        self.player.spawn()
        self.hud = HUD(self.player)
        self.hud.update_stats_container()
        self.hud.update_status_bars()
        self.map = TutorialMap()

    @property
    def name(self) -> str:
        return "Tutorial"

    @property
    def fades(self) -> bool:
        return False

    @property
    def color(self) -> color:
        return rgb(0, 0, 117)
