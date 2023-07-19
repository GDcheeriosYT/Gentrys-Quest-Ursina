from ursina import *


class LocationButton(Button):
    def __init__(self, location_name: str, parent: Entity):
        super().__init__(
            location_name,
            color=color.gold,
            origin=(-0.5, 0),
            position=(-0.48, 0),
            scale=(0.4, 0.2),
            parent=parent
        )
