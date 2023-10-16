from ursina import *


class MapDetailContainer(Button):
    def __init__(self, preview: Entity, info: Text, *args, **kwargs):
        super().__init__(
            model=Quad(0.02),
            *args,
            **kwargs
        )

        preview.parent = self
        preview.scale = (0.05, 0.18)
        preview.position = (-0.3, 0)

        info.parent = self
        info.scale = 1.5, 4
        info.origin = (0.5, 0.5)
        info.position = (0.45, 0.5)

        print(preview.scale, info.scale)

    def on_click(self):
        self
