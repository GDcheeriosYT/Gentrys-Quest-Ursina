from ursina import *

from utils.Event import Event

from .TestMethodButton import TestMethodButton


class Test:
    screen = None

    def __init__(self, class_type):
        self.name = class_type.__name__
        self.method_buttons = []
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

    def load(self):
        """
        Load the test
        """
        self.on_load()

    def unload(self):
        """
        Unload the test
        """

        [destroy(button) for button in self.method_buttons]
        self.method_buttons.clear()
        self.on_unload()

    def reload(self):
        self.unload()
        self.load()

    def on_destroy(self):
        self.unload()