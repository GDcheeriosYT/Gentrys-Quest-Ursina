from ursina import *

import Game

from Graphics.Container import Container


class GachaMenu(Entity):
    def __init__(self, parent):
        super().__init__(
            model="quad",
            color=color.clear,
            parent=parent
        )

        self.gachas = Game.content_manager.gachas

        self.selected_gacha = self.gachas[0]

        self.amount = 1
        self.amount_container = Container(
            position=(-0.25, 0.35),
            scale=(0.1, 0.25),
            parent=self
        )
        self.amount_down = Button(
            "-",
            scale=(0.25, 0.25),
            position=(-0.5, 0),
            parent=self.amount_container
        )
        self.amount_down.on_click = lambda: self.increase_amount(False)
        self.amount_text = Text(
            str(self.amount),
            scale=(7, 7),
            position=(0, 0),
            origin=(0, 0),
            color=color.black,
            parent=self.amount_container
        )
        self.amount_text_text = Text(
            "Amount",
            position=(0, 0.25),
            scale=(5, 5),
            origin=(0, 0),
            color=color.black,
            parent=self.amount_container
        )
        self.amount_up = Button(
            "+",
            scale=(0.25, 0.25),
            position=(0.5, 0),
            parent=self.amount_container
        )
        self.amount_up.on_click = lambda: self.increase_amount(True)

    def increase_amount(self, increase: bool):
        self.amount += 1 if increase else -1
        if self.amount < 1:
            self.amount = 1

        self.amount_text.text = str(self.amount)
