from ursina import *


class Container(Entity):
    def __init__(self, position: tuple = (0, 0), origin: tuple = (0, 0)):
        super().__init__(
            parent=camera.ui,
            position=position,
            origin=origin
        )

    def add_entity(self, entity: Entity):
        entity.parent = self
        # do something