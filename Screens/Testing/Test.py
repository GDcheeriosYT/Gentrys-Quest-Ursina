import traceback

from ursina import *

import Game
from utils.Event import Event

from .TestSliderVariable import TestSliderVariable
from .TestMethodButton import TestMethodButton


class Test:
    screen = None

    def __init__(self, class_type):
        self.name = class_type.__name__
        self.method_buttons = []
        self.variables = []
        self.on_load = Event("OnLoad")
        self.on_unload = Event("OnUnload")

    def make_button(self, name: str, event: 'Callable'):
        self.method_buttons.append(TestMethodButton(name, event))

    def get_button(self, name: str = None, index: int = None):
        if name is not None:
            for button in self.method_buttons:
                if name == button.name:
                    return button

        if index is not None:
            return self.method_buttons[index]

        return None

    def make_slider(self, name: str, min, max, default):
        self.variables.append(TestSliderVariable(name, min, max, default))

    def get_variable(self, name: str):
        for variable in self.variables:
            if variable.name == name:
                return variable.value

    def load(self):
        """
        Load the test
        """

        try:
            self.on_load()
        except Exception as e:
            Game.exception_handler.handle_exception(e)

    def unload(self):
        """
        Unload the test
        """

        [destroy(button) for button in self.method_buttons]
        [destroy(variable) for variable in self.variables]
        self.method_buttons.clear()
        self.variables.clear()

        try:
            self.on_unload()
        except Exception as e:
            Game.exception_handler.handle_exception(e)

    def reload(self):
        self.unload()
        self.load()

    def on_destroy(self):
        self.unload()
