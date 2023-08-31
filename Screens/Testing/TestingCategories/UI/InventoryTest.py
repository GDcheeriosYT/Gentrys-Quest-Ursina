from ursina import *

from ...Test import Test

import Game
from Graphics.UIs.Inventory.Inventory import Inventory
from Content.Characters.TestCharacter import TestCharacter
from Content.ArtifactFamilies.TestFamily.TestArtifact import TestArtifact
from Content.Weapons.Knife.Knife import Knife


class InventoryTest(Test):
    def __init__(self):
        super().__init__(Inventory)

        self.inventory = None
        self.inventory: Inventory

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        def create_inventory():
            if not self.inventory:
                self.inventory = Inventory(True, Test.screen)
                self.inventory.update_player()

        self.make_button("Create Inventory", create_inventory)
        self.get_button(index=0).on_click()

        self.make_button("Add Money", lambda: Game.user.add_money(100))
        self.make_button("Add Character", lambda: Game.user.add_character(TestCharacter()))
        self.make_button("Add Artifact", lambda: Game.user.add_artifact(TestArtifact()))
        self.make_button("Add Weapon", lambda: Game.user.add_weapon(Knife()))

    def _unload(self):
        destroy(self.inventory)
