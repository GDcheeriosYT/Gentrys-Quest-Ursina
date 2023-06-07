from ursina import *


class Container(Entity):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(
            parent=camera.ui if not parent else parent,
            *args,
            **kwargs
        )

    def highlight(self):
        self.color = rgb(17, 17, 17, 125)
