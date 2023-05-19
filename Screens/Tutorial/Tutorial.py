from ursina import *
from ..Screen import Screen
from Graphics.UIs.HUD.HUD import HUD
import Game
from .Map.TutorialMap import TutorialMap
from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen
from Content.Enemies.AngryPedestrian.AngryPedestrian import AngryPedestrian
from Graphics.Containers.TextContainer import TextContainer
from .Map.Ramen import Ramen
from ursina.curve import *


class Tutorial(Screen):
    def __init__(self):
        super().__init__()
        self.on_show += self._show
        self.phase = 0

    def _show(self):
        self.player = Game.user.get_equipped_character()
        self.player.swap_weapon(BraydensOsuPen())
        self.player.can_move = False
        self.map = TutorialMap()
        text_container = TextContainer()
        text_container.set_text("It's 10pm...", 5)
        camera.position = (0, -10, -20)
        camera.animate_position((0, 0, -20), 4, curve=linear)
        invoke(self.player.spawn, delay=5)
        invoke(self.player.toggle_movement, delay=10)
        self.hud = HUD(self.player)
        self.hud.hide_elements()
        text_container.schedule_text(f"{self.player.name} is at a\nconvenience store buying ramen noodles.", 5, 5)
        text_container.schedule_text(f"He picks up some ramen.", 10, 5)
        invoke(lambda: Ramen(position=(6, 0)), delay=10)
        invoke(self.show_controls, delay=9)
        npc = AngryPedestrian()
        npc.follow_entity(self.player)
        #invoke(npc.spawn, delay=12)

    def show_controls(self):
        movement = Text(
            "Movement\nW A S D",
            position=(-0.8, 1),
            scale=(4, 4),
            parent=camera.ui,
        )
        movement.animate_position((-0.8, 0.5), duration=2, curve=linear)
        invoke(lambda: movement.fade_out(duration=2), delay=4)
        destroy(movement, 8)

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
