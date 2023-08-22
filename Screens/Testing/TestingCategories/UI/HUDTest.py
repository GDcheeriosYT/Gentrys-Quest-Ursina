from ursina import *

from ...Test import Test

from Graphics.UIs.HUD.HUD import HUD
from Content.Characters.TestCharacter import TestCharacter
from Content.Effects.Burn.Burn import Burn


class HUDTest(Test):
    def __init__(self):
        super().__init__(HUD)

        self.test_player = None
        self.test_player: TestCharacter

        self.hud = None
        self.hud: HUD

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        self.test_player = TestCharacter(parent=Test.screen)
        self.test_player.scale = (0.2, 0.2)
        self.test_player.spawn()

        def create_hud():
            if not self.hud:
                self.hud = HUD(self.test_player, parent=Test.screen)

        self.make_button("Create HUD", create_hud)
        self.get_button(index=0).on_click()
        self.make_button("Damage Player", lambda: self.test_player.damage(100))
        self.make_button("Heal Player", lambda: self.test_player.heal(100))
        self.make_button("Level Up Player", self.test_player.level_up)
        self.make_button("Add XP", lambda: self.test_player.add_xp(100))
        self.make_button("Burn Player", lambda: self.test_player.apply_effect(Burn(7)))

    def _unload(self):
        self.hud.end()
        destroy(self.test_player)
