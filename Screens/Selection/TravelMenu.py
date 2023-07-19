from ursina import *

import Game
from .LocationButton import LocationButton


class TravelMenu(Entity):
    def __init__(self, parent):
        super().__init__(
            color=color.clear,
            parent=parent
        )

        self.locations = []
        self.selected_location = None
        self.area_info = None

        position_y = 0.4
        for location in Game.content_manager.locations:
            print(location().name)
            area_button = LocationButton(location().name, self)
            area_button.y = position_y
            self.locations.append(area_button)
            position_y -= 0.1
