from ursina import *


class TitleText(Text):
    def __init__(self, text: str, container:Entity = None):
        super().__init__(
            text,
            position=container.position + (0, 0.15, 0) if container else (0, 0.15, 0),
            origin=(0, 0),
            color=color.black,
            text_style="bold",
            size=5,
        )
