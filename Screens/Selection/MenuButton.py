from ursina import *
from utils.Event import Event

from Graphics.GameButton import GameButton


class MenuButton(GameButton):
    def __init__(self, text: str = "menu button", *args, **kwargs):
        super().__init__(
            text,
            scale=(0.5, 0.5),
            *args,
            **kwargs
        )

        self.active = False
        self.active_color = color.gray
        self.deactive_color = color.black
        self.on_click_event = Event('OnClick', 0)

    def activate(self):
        self.active = True
        self.update_color()

    def deactivate(self):
        self.active = False
        self.update_color()

    def on_click(self):
        self.on_click_event()

    def update_color(self):
        if self.active:
            self.color = self.active_color
        else:
            self.color = self.deactive_color
