from ursina import *

from Content.Locations.TestLocation.TestLocation import TestLocation


class TravelMenu(Entity):
    def __init__(self, parent):
        super().__init__(
            color=color.clear,
            parent=parent
        )

        self.locations = []
        self.selected_location = None
        self.area_info = None

        for locations in self.locations:
            area_button = Button(
                area.name
            )
