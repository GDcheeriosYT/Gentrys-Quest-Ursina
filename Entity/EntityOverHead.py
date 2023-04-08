from ursina import *
from ursina.prefabs.health_bar import HealthBar


class EntityOverhead(Entity):
    def __init__(self, name: str, health: int, is_player: bool = False):
        super().__init__(
            parent=camera.ui,
            origin=(0, 0),
            scale=(1, 1),
            position=(0, 0.1)
        )
        self.name = Text(name, parent=self, position=(0, 0.5))
        self.health_bar = HealthBar(max_value=health, parent=self, position=(0, -0.5)) if is_player else None
