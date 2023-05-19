from ursina import *

import Game
from .GasStation import GasStation
from .ParkingLot import ParkingLot


class TutorialMap(Entity):
    def __init__(self):
        super().__init__(
            # model='quad',
            # color=color.clear,
            # collider='box',
            # scale=(20, 60),
            # parent=self
        )
        self.gas_station = GasStation()
        self.parking_lot = ParkingLot()
