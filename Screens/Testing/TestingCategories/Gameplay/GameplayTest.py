from ursina import *

import Game

from ...Test import Test
from ...TestTypes import TestTypes

from Screens.Gameplay.Gameplay import Gameplay


class GameplayTest(Test):
    def __init__(self):
        super().__init__(Gameplay, TestTypes.NotScreenTest)
        self.on_load += self._load
        self.on_unload += self._unload

        self.gameplay = None
        self.gameplay: Gameplay

    def _load(self):
        Game.selected_area = Game.content_manager.get_location("Test Location").areas[0]
        Game.user.get_equipped_character().swap_weapon(Game.content_manager.get_weapon("Brayden's Osu Pen"))

        def initialize_gameplay():
            if not self.gameplay:
                self.gameplay = Gameplay(test=True)

        def load_gameplay():
            self.gameplay.show()

        def apply_variables():
            self.gameplay.map.enemy_limit = self.get_variable("Enemy Limit")
            self.gameplay.map.difficulty = self.get_variable("Difficulty")
            self.gameplay.map.enemy_pool.destroy()
            self.gameplay.map.unload()
            self.gameplay.map.load()

        self.make_button("Initialize Gameplay", initialize_gameplay)
        self.make_button("Load Gameplay", load_gameplay)
        self.get_button(index=0).on_click()
        self.get_button(index=1).on_click()
        self.make_button("Spawn Enemies", self.gameplay.map.spawn)
        self.make_button("Kill All Enemies", self.gameplay.map.kill_all_enemies)
        self.make_slider("Difficulty", 0, 5, 0, 1)
        self.make_slider("Enemy Limit", 1, 50, 5, 1)
        self.make_button("Apply Variables", apply_variables)

    def _unload(self):
        self.gameplay.hide()
        destroy(self.gameplay)
