from ...Category import Category

from .HUDTest import HUDTest


class UI(Category):
    def __init__(self):
        super().__init__(
            "UI",
            [
                HUDTest(),
            ]
        )
