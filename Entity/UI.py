from ursina import *
from ursina.prefabs.health_bar import HealthBar

class UI(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )
        self.health_bar = HealthBar(position=(-0.25, -0.40))