import Game
from Screens.Screen import Screen
from Graphics.UIs.HUD.HUD import HUD
from Graphics.UIs.Inventory.Inventory import Inventory
from Content.Maps.TestMap import TestMap
from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen
from ursina import *


class Gameplay(Screen):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.player = None
        self.hud = None
        self.inventory = None
        self.in_inventory = False
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
        self.inventory = Inventory()
        self.inventory.disable()
        self.player.spawn()
        weapon = BraydensOsuPen()
        # self.player.swap_weapon(weapon)
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
            # self.map.spawn_sequence()
            self.spawned = True
            invoke(self.toggle_spawned, delay=1)

        if self.player != Game.user.get_equipped_character():
            self.player.despawn()
            destroy(self.hud)
            self.player = Game.user.get_equipped_character()
            self.player.spawn()
            self.hud = HUD(self.player)
            self.hud.hide_elements()

    def input(self, key):
        if key == "c":
            if not self.in_inventory:
                self.map.can_spawn = False
                self.hud.hide_elements()
                self.player.disable()
                self.map.manage_entities(False, False)
                self.inventory.enable()
                self.in_inventory = True
            else:
                self.map.can_spawn = True
                self.hud.show_elements()
                self.player.enable()
                self.map.manage_entities(False, True)
                self.inventory.disable()
                self.in_inventory = False
