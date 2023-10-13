from ursina import *

import Game

from ...Test import Test
from ...TestTypes import TestTypes

from Location.Map import Map
from Screens.Gameplay.Gameplay import Gameplay


class GameplayTest(Test):
    def __init__(self):
        super().__init__(Gameplay, TestTypes.NotScreenTest)
        self.on_load += self._load
        self.on_unload += self._unload

        Game.selected_area = Game.content_manager.get_location("Test Location").areas[0]

        self.gameplay = None
        self.gameplay: Gameplay

        print("selected area\n\n\n\n\n\n\n\n\n",Game.selected_area)

    def _load(self):
        def initialize_gameplay():
            if not self.gameplay:
                self.gameplay = Gameplay(test=True)

        def load_gameplay():
            self.gameplay.show()

        self.make_button("Initialize Gameplay", initialize_gameplay)
        self.make_button("Load Gameplay", load_gameplay)
        self.get_button(index=0).on_click()
        self.get_button(index=1).on_click()
        self.make_button("Spawn Enemies", self.gameplay.map.spawn)
        self.make_button("Kill All Enemies", self.gameplay.map.kill_all_enemies)


    def _unload(self):
        self.gameplay.hide()
        destroy(self.gameplay)
