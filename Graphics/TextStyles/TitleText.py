from ursina import *


class TitleText(Text):
    def __init__(self, text: str, hidden=False):
        super().__init__(
            text,
            position=(0, 0.15, 0),
            origin=(0, 0),
            color=color.black,
            text_style="bold",
            scale=(5, 5),
            alpha=0 if hidden else 1
        )


