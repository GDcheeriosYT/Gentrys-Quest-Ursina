from ursina import *

from Screens.Screen import Screen
from Graphics.Container import Container


class Testing(Screen):
    def __init__(self):
        super().__init__(
            False
        )

        self.screen = Container(
            position=(0.4, -0.1),
            scale=(0.6, 0.6),
            parent=self
        )

        # self.category_container = Container(
        #     position=(0, 0.45),
        #     scale=(1, 0.35),
        #     parent=self
        # )

        self.categories = []

        for category in self.categories:
            Button(category.name)
