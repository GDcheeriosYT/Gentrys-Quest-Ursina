from ursina import *

import Game

from Location.MapDetailContainer import MapDetailContainer

from .EditorStates import EditorStates


class MapSelector(Entity):
    def __init__(self, parent_screen):
        super().__init__(
            model=Quad(0.02),
            color=rgb(17, 17,  17, 200),
            scale=(0.6, 0.8),
            parent=camera.ui
        )

        self.parent_screen = parent_screen

        self.maps = []

        self.load_maps()
        self.display_maps()

    def load_maps(self):
        for location in Game.content_manager.locations:
            location = location()
            for map in location.areas:
                self.maps.append(map)

    def display_maps(self):
        position_y = 0.35
        def assign_click(container, map):

            def click():
                self.parent_screen.editor.map_name = map.name
                self.parent_screen.editor.objects = map.entities
                self.parent_screen.editor.enemies = map.enemies
                self.parent_screen.editor.state = EditorStates.MapMetadata

            container.on_click

        for map in self.maps:
            container = MapDetailContainer(map.generate_preview(), Text(map.get_metadata()), parent=self, scale=(0.98, 0.2), position=(0, position_y))

            position_y -= 0.2
