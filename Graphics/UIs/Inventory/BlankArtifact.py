from ursina import *


class BlankArtifact(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "empty",
            color=rgb(0, 0, 0, 160),
            *args,
            **kwargs
        )
