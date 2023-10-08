from ursina import *

from Graphics.GameButton import GameButton

class TabButton(GameButton):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(
            text,
            model=Quad(0.03),
            origin=(0, 0.5),
            color=rgb(117, 117, 117),
            scale=(0.35, 0.15),
            parent=camera.ui,
            *args,
            **kwargs
        )
