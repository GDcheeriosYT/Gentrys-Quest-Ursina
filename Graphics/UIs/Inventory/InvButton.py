from ursina import *


class InvButton(Button):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(
            text,
            scale=(0.15, 0.15),
            color=color.black,
            *args,
            **kwargs
        )
