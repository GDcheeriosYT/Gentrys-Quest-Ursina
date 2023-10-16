from ursina import *


class MapMetadata(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model=Quad(0.02),
            color=color.dark_gray,
            *args,
            **kwargs
        )
