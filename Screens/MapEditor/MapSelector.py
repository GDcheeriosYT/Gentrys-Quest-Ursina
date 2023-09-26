from ursina import *

import Game

from Location.MapDetailContainer import MapDetailContainer


class MapSelector(Entity):
    def __init__(self):
        super().__init__(
            model="quad",
            color=rgb(17, 17,  17, 200),
            scale=(0.6, 0.8),
            parent=camera.ui
        )

        self.maps = []

        self.load_maps()
        self.display_maps()

    def load_maps(self):
        for location in Game.content_manager.locations:
            location = location()
            for map in location.areas:\
                self.maps.append(map)

    def display_maps(self):
        position_y = 0.3
        for map in self.maps:
            MapDetailContainer(map.generate_preview(), Text(map.get_metadata()), parent=self, scale=(1, 0.2), position=(0, position_y))
            position_y -= 0.2
