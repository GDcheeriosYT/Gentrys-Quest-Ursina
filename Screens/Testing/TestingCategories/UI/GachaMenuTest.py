from ursina import *

from ...Test import Test

from Screens.Selection.GachaMenu import GachaMenu


class GachaMenuTest(Test):
    def __init__(self):
        super().__init__(GachaMenu)
        self.gacha_menu = None
        self.gacha_menu: GachaMenu

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        def create_menu():
            if not self.gacha_menu:
                self.gacha_menu = GachaMenu(Test.screen)

        self.make_button("Create Menu", create_menu)
        self.get_button(index=0).on_click()

        self.make_button("Increase Amount", lambda: self.gacha_menu.increase_amount(True))
        self.make_button("Decrease Amount", lambda: self.gacha_menu.increase_amount(False))

    def _unload(self):
        destroy(self.gacha_menu)