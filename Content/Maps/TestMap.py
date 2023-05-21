from ursina import *
from Location.Map import Map


grass = Entity(
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
