from ...Category import Category

from .HUDTest import HUDTest
from .InventoryTest import InventoryTest
from .GachaMenuTest import GachaMenuTest


class UI(Category):
    def __init__(self):
        super().__init__(
            "UI",
            [
                HUDTest(),
                InventoryTest(),
                GachaMenuTest()
            ]
        )
