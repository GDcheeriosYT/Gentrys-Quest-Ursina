from ursina import *
from .GasStation import GasStation


class TutorialMap(Entity):
    def __init__(self):
        super().__init__()

        self.gas_station = GasStation()
