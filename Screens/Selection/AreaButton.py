from ursina import *

from utils.Event import Event


class AreaButton(Button):
    def __init__(self, area_name: str, parent: Entity):
        super().__init__(
            area_name,
            origin=(-0.5, 0),
            position=(-0.48, 0),
            scale=(0.4, 0.2),
            parent=parent
        )

        self.on_click_event = Event('OnClick', 0)
        self.on_click = self.on_click_event
