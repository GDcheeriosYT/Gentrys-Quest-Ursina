from ursina import *


class MapPreview(Entity):
    def __init__(self, map):
        super().__init__()
        self.objects = []
        for object in map.entities:
            object.parent = self
