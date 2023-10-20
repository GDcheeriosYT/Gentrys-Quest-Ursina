from ursina import *

import Game

from Screens.Screen import Screen
from Graphics.UIs.HUD.HUD import HUD
from Graphics.UIs.Inventory.Inventory import Inventory


class Gameplay(Screen):
    def __init__(self, test: bool = False):
        super().__init__()
        self.player = None
        self.hud = None
        self.inventory = None
        self.in_inventory = False
        self.map = None
        self.time_tracker = time.time()
        self.test = test

        self.on_show += self._on_show
        self.on_hide += self._on_hide

    @property
    def name(self) -> str:
        return "Gameplay"

    @property
    def color(self):
        return color.gray

    def levelup_score_manager(self):
        Game.score_manager.add_level(self.player.experience.level)

    def diff_check(self):
        self.map.calculate_difficulty(self.player)

    def _on_show(self):
        Game.score_manager.reset_score()
        self.map = Game.selected_area
        self.player = Game.user.get_equipped_character()
        self.player.on_level_up += self.levelup_score_manager
        self.hud = HUD(self.player)
        if self.test:
            self.hud.scale = (self.hud.scale[0]*0.8, self.hud.scale[1]*0.8)
            self.hud.position = (0, -0.1)

        self.inventory = Inventory()
        if self.test:
            self.inventory.scale = (self.hud.scale[0]*0.75, self.hud.scale[1]*0.75)

        self.inventory.update_player()
        self.inventory.disable()
        self.map.load()
        self.player.spawn()
        self.player.on_level_up += self.diff_check
        self.time_started = time.time()
        self.spawned = False

    def _on_hide(self):
        if self.map:
            self.map.unload()

        if self.hud:
            self.hud.end()

        if self.player:
            self.player.disable()
            self.player.on_level_up -= self.levelup_score_manager
            self.player.on_level_up -= self.diff_check

        if self.inventory:
            destroy(self.inventory)

        camera.position = (0, 0)

    def toggle_spawned(self):
        self.spawned = False

    def spawn_ready(self):
        difficulty_factor = 1.0 / self.map.current_difficulty
        spawn_interval = self.map.spawn_delay * difficulty_factor
        if time.time() - self.time_tracker >= spawn_interval:
            self.set_starting_time()
            return True
        else:
            return False

    def set_starting_time(self):
        self.time_tracker = time.time()

    def update(self):
        if self.player.spawned:
            camera.position = (self.player.x, self.player.y, -20)

        if self.spawn_ready() and self.map.can_spawn and not self.test:
            self.map.enemy_pool.shuffle()
            self.map.spawn_sequence()

        self.map.artifact_check()

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
