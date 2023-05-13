from ursina import *


class AreaOfEffect(Entity):
    def __init__(self, size, *args, **kwargs):
        super().__init__(
            scale=(size, size),
            collider="sphere"
        )

    def update(self):
        pass
