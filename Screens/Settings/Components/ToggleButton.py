from ursina import *

from Graphics.GameButton import GameButton


class ToggleButton(GameButton):
    def __init__(self, toggled: bool, on_text: str, off_text: str, *args, **kwargs):
        super().__init__(
            on_text if toggled else off_text,
            color=color.gray if toggled else color.black,
            scale=(0.1, 0.05),
            *args,
            **kwargs
        )
        self.toggled = toggled
        self.on_text = on_text
        self.off_text = off_text

    def on_click(self):
        self.toggled = not self.toggled
        if self.toggled:
            self.text = self.on_text
            self.color = color.gray
        else:
            self.text = self.off_text
            self.color = color.black
