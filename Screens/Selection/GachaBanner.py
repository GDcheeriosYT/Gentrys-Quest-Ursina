from ursina import *

from Gacha.Gacha import Gacha

from Graphics.GameButton import GameButton


class GachaBanner(GameButton):
    def __init__(self, gacha: Gacha, *args, **kwargs):
        super().__init__(
            model="quad",
            scale=(0.5, 0.9),
            color=color.clear,
            highlight_color=color.clear,
            *args,
            **kwargs
        )

        # metadata
        self.name = gacha.name
        self.cost = gacha.cost
        self.character_amount = len(gacha.characters)
        self.weapon_amount = len(gacha.weapons)

        # entity
        self.background = Entity(
            model=Quad(0.03),
            color=color.black,
            position=(0, 0, -1),
            parent=self
        )

        self.outline = Entity(
            model=Quad(0.03),
            color=color.white,
            position=(0, 0, 1),
            scale=(1.02, 1.02),
            parent=self.background
        )

        self.upper_line = Entity(
            model="quad",
            color=color.white,
            scale=(1, 0.01),
            position=(0, 0.4, -1),
            parent=self.outline,
        )

        self.bottom_line = Entity(
            model="quad",
            color=color.white,
            scale=(1, 0.01),
            position=(0, -0.4, -1),
            parent=self.outline,
        )

        self.money_text = Text(
            f"${self.cost}",
            position=(0, 0.45, -1),
            origin=(0, 0),
            scale=(4, 2),
            color=color.white,
            parent=self.background
        )

        self.amount_text = Text(
            f"{self.character_amount} characters\n{self.weapon_amount} weapons",
            position=(0, -0.45, -1),
            origin=(0, 0),
            scale=(4, 1.5),
            color=color.white,
            parent=self.background
        )

    def select(self):
        self.outline.color = color.yellow
        self.bottom_line.color = color.yellow
        self.upper_line.color = color.yellow

    def deselect(self):
        self.outline.color = color.white
        self.bottom_line.color = color.white
        self.upper_line.color = color.white
