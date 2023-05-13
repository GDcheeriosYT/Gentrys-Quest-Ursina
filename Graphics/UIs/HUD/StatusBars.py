from ursina import *
from ursina.prefabs.health_bar import HealthBar
from Graphics.Container import Container
from .ExperienceBar import ExperienceBar


class StatusBars(Container):
    def __init__(self):
        super().__init__(
            origin=(0, -0.5),
            scale=(0.8, 0.2),
            position=(-0.3, -0.5)
        )
        self._health_bar = HealthBar(
            max_value=100,
            scale=(1, 0.3),
            position=(-0.5, 0.5),
            parent=self
        )
        self._experience_container = Container(
            position=(0, 0.95),
            parent=self
        )
        self._level = Text(
            "lvl. 0",
            position=(-0.45, 0),
            origin=(0.5, 0.5),
            color=rgb(0, 0, 0),
            scale=(3.3, 12),
            parent=self._experience_container
        )
        self._experience_bar = ExperienceBar(
            max_value=100,
            scale=(0.9, 0.3),
            value=0,
            position=(-0.41, 0),
            parent=self._experience_container
        )

    def update_data(self, player):
        self._health_bar.max_value = int(player.stats.health.get_value())
        self._health_bar.value = int(player.stats.health.current_value)
        self._level.text = f"lvl. {player.experience.level}"
        self._experience_bar.update_data(player.experience.xp, player.experience.get_xp_required(player.star_rating))

