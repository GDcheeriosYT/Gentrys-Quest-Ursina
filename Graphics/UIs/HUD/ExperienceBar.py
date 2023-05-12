from ursina import *
from ursina.prefabs.health_bar import HealthBar


class ExperienceBar(HealthBar):
    def __init__(self, *args, **kwargs):
        super().__init__(
            bar_color=rgb(0, 0, 255),
            *args,
            **kwargs
        )

    def update_data(self, current_xp: int, required_xp: int):
        self.value = int(current_xp)
        self.max_value = int(required_xp)
