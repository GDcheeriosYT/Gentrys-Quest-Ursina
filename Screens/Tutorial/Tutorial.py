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
        self.phase = 0

    def _show(self):
        self.player = Game.user.get_equipped_character()
        self.player.swap_weapon(BraydensOsuPen())
        self.map = TutorialMap()
        text_box = Text(
            "It's 10pm",
            position=(-0.5, -0.5),
            origin=(-0.5, 0),
            parent=text_container
        )
        destroy(text_box, 5)
        camera.position = (0, -10, -20)
        camera.animate_position((0, 0, -20), 4)
        invoke(self.player.spawn, delay=5)
        self.hud = HUD(self.player)
        self.hud.hide_elements()
        text_box1 = Text(
            f"{self.player.name} is at a convenience store buying ramen noodles",
            position=(-0.5, 0.5),
            origin=(-0.5, 0),
            parent=text_container
        )
        text_box1.disable()
        invoke(text_box1.enable, delay=5.3)
        destroy(text_box1, 10)

    @property
    def name(self) -> str:
        return "Tutorial"

    @property
    def fades(self) -> bool:
        return True

    @property
    def color(self) -> color:
        return rgb(0, 0, 117)

    def input(self, key):
        if key == "left mouse":
            self.phase += 1
