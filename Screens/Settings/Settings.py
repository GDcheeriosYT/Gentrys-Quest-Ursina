from ursina import *
from ..Screen import Screen


class Settings(Screen):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return "Settings"
