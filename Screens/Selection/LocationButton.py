from ursina import *

from utils.Event import Event
from Graphics.GameButton import GameButton


class LocationButton(GameButton):
    def __init__(self, location_name: str, parent: Entity):
        super().__init__(
            location_name,
            origin=(-0.5, 0),
            position=(-0.5, 0),
            scale=(1, 0.2),
            parent=parent
        )

        self.on_click_event = Event('OnClick', 0)
        self.on_click = self.on_click_event
