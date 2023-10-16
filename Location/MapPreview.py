from ursina import *


class MapPreview(Entity):
    def __init__(self, map):
        super().__init__(
            position=(0, 0, -1)
        )
        self.objects = []
        for object in map.entities:
            object.enable()
            object.scale = (object.scale[0]*0.1, object.scale[1]*0.1)
            object.parent = self
