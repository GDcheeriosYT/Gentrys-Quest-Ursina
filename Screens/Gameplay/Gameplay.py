import Game
from Screens.Screen import Screen
from Graphics.UIs.HUD.HUD import HUD
from Content.Maps.TestMap import TestMap
from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen
from ursina import *


class Gameplay(Screen):
    def __init__(self):
        super().__init__()

        self.player = None
        self.hud = None
        self.map = None
        self.time_started = None

        self.on_show += self._on_show

    @property
    def name(self) -> str:
        return "Gameplay"

    @property
    def color(self):
        return color.gray

    def _on_show(self):
        self.player = Game.user.get_equipped_character()
        self.hud = HUD(self.player)
        self.player.spawn()
        self.player.swap_weapon(BraydensOsuPen())
        self.map = TestMap()
        self.time_started = time.time()
        self.map.load()
        self.spawned = False

    def toggle_spawned(self):
        self.spawned = False

    def update(self):
        time_elapsed = time.time() - self.time_started
        # print(time_elapsed, self.map.current_difficulty)
        # print(int(time_elapsed) % self.map.current_difficulty)
        # print(int(time_elapsed) % 10)
        if int(time_elapsed) % 10 == self.map.current_difficulty and not self.spawned:
            self.map.spawn_sequence()
            self.spawned = True
            invoke(self.toggle_spawned, delay=1)
