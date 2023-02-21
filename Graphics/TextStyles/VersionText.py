from ursina import *


class VersionText(Text):
    def __init__(self, text: str):
        super().__init__(
            text,
            position=window.bottom_left,
            origin=(-0.6, -1),
            color=color.black,
            text_style="bold"
        )
