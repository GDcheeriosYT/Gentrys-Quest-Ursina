from ursina import *

from Screens.Screen import Screen
from Graphics.Container import Container
from utils.Event import Event

from .TestingCategories.Entity.Entity import Entity
from .TestingScreen import TestingScreen


class Testing(Screen):
    def __init__(self):
        super().__init__(
            False
        )

        self.screen = TestingScreen(
            position=(0.35, -0.1),
            scale=(1, 0.7),
            color=color.gray,
            parent=self
        )

        self.category_container = Container(
            position=(0, 0.45),
            scale=(1.5, 0.35),
            parent=self
        )

        self.tests_container = Container(
            position=window.left,
            origin=(-0.5, 0),
            scale=(0.35, 0.5),
            parent=self
        )

        self.tests_option_container = Container(
            position=(-0.55, 0),
            origin=(0.5, 0),
            scale=(0.25, 1),
            parent=self.screen
        )

        self.categories = [Entity()]

        self.tests = []

        self.screen_info_text = Text(
            "",
            position=(-0.5, 0.5),
            origin=(-0.5, 0.5),
            parent=self.screen
        )

        self.category = None

        self.change_category(Entity())

        x = 0
        space_coefficient = 1
        scale_x = 1 / (space_coefficient * len(self.categories))
        center_offset = (len(self.categories) - 1) * scale_x / 2
        for category in self.categories:
            button = Button(
                category.name,
                model='quad',
                parent=self.category_container
            )
            button.scale = (scale_x - (scale_x * 0.1), 0.4) if len(self.categories) > 2 else (0.4, 0.4)
            button.text_entity.scale = (0.3, 0.5)
            button.position = ((x * scale_x) - center_offset, -0.1)
            button.on_click = lambda: self.change_category(category)

            x += 1

    @property
    def color(self):
        return color.rgb(35, 35, 35)

    def change_category(self, category):
        self.category = category
        self.load_category()

    def load_category(self):
        self.clear_tests()
        for test in self.category.tests:
            def assign_click(button, index):
                clicky = Event("onClick", 0)
                clicky += lambda: self.category.select_test(index)
                clicky += self.update_screen_text
                button.on_click = clicky

            index = self.category.tests.index(test)

            button = Button(
                test.name,
                position=(0.85, 0.5 - (index * 0.12)),
                scale=(1, 0.1),
                parent=self.tests_container
            )
            assign_click(button, index)
            self.tests.append(button)

        self.update_screen_text()

    def clear_tests(self):
        [destroy(test) for test in self.tests]

    def update_screen_text(self):
        self.screen_info_text.text = f"Testing {self.category.name}.{self.category.selected_test.name}"
