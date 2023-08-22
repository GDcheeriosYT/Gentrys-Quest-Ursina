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
        self.player = None
        self.hud = None
        self.inventory = None
        self.in_inventory = False
        self.map = None
        self.time_started = None

        self.on_show += self._on_show
        self.on_hide += self._on_hide

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
        self.inventory.update_player()
        self.inventory.disable()
        self.player.spawn()
        self.map = Game.selected_area
        self.time_started = time.time()
        self.map.load()
        invoke(self.map.spawn_sequence, delay=5)
        self.spawned = False

    def _on_hide(self):
        if self.map:
            self.map.unload()

        if self.hud:
            self.hud.end()

        destroy(self.inventory)

    def toggle_spawned(self):
        self.spawned = False

    def update(self):
        if self.player.spawned:
            camera.position = (self.player.x, self.player.y, -20)
        time_elapsed = time.time() - self.time_started
        difficulty_factor = 1.0 / self.map.current_difficulty
        next_spawn_time = self.map.spawn_delay
        spawn_interval = self.map.spawn_delay * difficulty_factor
        if time_elapsed >= next_spawn_time and self.map.can_spawn:
            self.map.spawn_sequence()
            # self.spawned = True
            # self.spawned = False

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
                self.map.toggle_enemies()
                self.inventory.enable()
                self.in_inventory = True
            else:
                self.map.can_spawn = True
                self.hud.show_elements()
                self.player.enable()
                self.map.toggle_enemies()
                self.inventory.disable()
                self.in_inventory = False
