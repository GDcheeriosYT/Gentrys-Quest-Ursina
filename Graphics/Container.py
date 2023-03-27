from ursina import *


class Container(Entity):
    def __init__(self, position: tuple = (0, 0), origin: tuple = (0, 0),
                 background_color: Color = color.rgba(0, 0, 0, 0), scale: tuple = (1, 1),
                 parent: Entity = None):
        super().__init__(
            model="quad",
            parent=camera.ui if not parent else parent,
            position=position,
            origin=origin,
            color=background_color,
            scale=scale
        )

    def highlight(self):
        self.color = rgb(17, 17, 17, 125)
