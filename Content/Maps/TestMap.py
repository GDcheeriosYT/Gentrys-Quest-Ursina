from ursina import *
from Location.Map import Map


grass = Entity(
    model='quad',
    position=(0, 0, 1),
    scale=(40, 40),
    color=color.green
)
grass.disable()


class TestMap(Map):
    def __init__(self):
        super().__init__(
            entities=[
                grass
            ]
        )
