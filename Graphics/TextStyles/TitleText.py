from ursina import *

from Graphics.GameText import GameText


class TitleText(GameText):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(
            text,
            position=(0, 0.15, 0),
            origin=(0, 0),
            text_style="bold",
            scale=(5, 5),
            *args,
            **kwargs
        )
