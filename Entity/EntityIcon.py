from ursina import *


class EntityIcon(Entity):
    def __init__(self, star_rating: int):
        super().__init__(
            scale=(0.2, 0.2),
            parent=camera.ui
        )

