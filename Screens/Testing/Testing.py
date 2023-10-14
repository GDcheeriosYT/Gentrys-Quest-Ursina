from ursina import *

from Screens.Screen import Screen
from Graphics.Container import Container
from utils.Event import Event

from .TestingCategories.Entity.Entity import Entity
from .TestingCategories.UI.UI import UI
from .TestingCategories.Components.Components import Components

from .TestingScreen import TestingScreen
from .Test import Test


class Testing(Screen):
    def __init__(self):
        super().__init__(
            False
        )

        self.screen = TestingScreen(
            position=(0.32, -0.1),
            scale=(0.7, 0.7),
            color=color.gray,
            parent=self
        )

        Test.screen = self.screen

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
            position=(-0.22, -0.3),
            origin=(0, 0.5),
            scale=(0.3, 1),
            parent=self
        )

        self.categories = [Entity(), UI(), Components()]

        self.tests = []

        self.screen_info_text = Text(
            "",
            position=(-0.5, 0.5, -1),
            origin=(-0.52, 0.55),
            parent=self.screen
        )

        self.category = None

        self.change_category(Entity())

        reload_button = Button(
            "Reload",
            parent=self.tests_option_container,
            position=(0, 0.57),
            scale=(1, 0.07)
        )

        reload_button.on_click = self.reload_test

        x = 0
        space_coefficient = 1
        scale_x = 1 / (space_coefficient * len(self.categories))
        center_offset = (len(self.categories) - 1) * scale_x / 2

        def assign_click(button, category):
            button.on_click = lambda: self.change_category(category)

        for category in self.categories:
            button = Button(
                category.name,
                model='quad',
                parent=self.category_container
            )
            button.scale = (scale_x - (scale_x * 0.1), 0.4) if len(self.categories) > 2 else (0.4, 0.4)
            button.text_entity.scale = (0.3, 0.5)
            button.position = ((x * scale_x) - center_offset, -0.1)
            assign_click(button, category)

            x += 1

    @property
    def color(self):
        return color.rgb(35, 35, 35)

    def change_category(self, category):
        if self.category:
            self.category.selected_test.unload()

        self.category = category
        self.category.selected_test.load()
        self.load_category()

    def load_category(self):
        """
        load a category
        """

        self.clear_tests()
        for test in self.category.tests:
            def assign_click(button, index):
                clicky = Event("onClick", 0)
                clicky += lambda: self.category.select_test(index)
                clicky += self.update_screen_text
                clicky += self.display_test
                button.on_click = clicky

            index = self.category.tests.index(test)

            button = Button(
                test.name,
                position=(0.53, 0.5 - (index * 0.12)),
                scale=(1, 0.1),
                parent=self.tests_container
            )
            assign_click(button, index)
            self.tests.append(button)

        self.update_screen_text()
        self.display_test()

    def display_test(self):
        """
        Load the selected test
        """

        y = 0.5

        for button in self.category.selected_test.method_buttons:
            button.parent = self.tests_option_container
            button.enable()
            button.position = (0, y)
            y -= 0.06

        for variable_handler in self.category.selected_test.variables:
            variable_handler.parent = self.tests_option_container
            variable_handler.enable()
            variable_handler.position = (0, y)
            y -= 0.06

    def clear_tests(self):
        [destroy(test) for test in self.tests]

    def update_screen_text(self):
        self.screen_info_text.text = f"Testing {self.category.name}.{self.category.selected_test.name}"

    def reload_test(self):
        self.category.selected_test.reload()
        self.display_test()