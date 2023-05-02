from ursina import *


class FadeScreen(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            color=rgb(0, 0, 0),
            position=(0, 0, -2),
            origin=(0, 0),
            scale=(2, 2),
            parent=camera.ui
        )

        self.fade_out(0, 0)