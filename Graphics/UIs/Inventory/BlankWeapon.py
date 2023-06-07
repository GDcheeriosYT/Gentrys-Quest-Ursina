from ursina import *


class BlankWeapon(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "blank",
            color=rgb(0, 0, 0, 160),
            scale=(0.15, 0.15),
            *args,
            **kwargs
        )


