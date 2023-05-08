from ursina import *
from ..Screen import Screen


class Play(Screen):
    def __init__(self):
        super().__init__()
        self.hud = Entity()