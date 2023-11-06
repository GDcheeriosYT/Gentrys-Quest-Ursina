from ursina import *
from ursina.prefabs.health_bar import HealthBar

import Game

from Graphics.Container import Container

from .EffectsContainer import EffectsContainer
from .ExperienceBar import ExperienceBar


class StatusBars(Container):
    def __init__(self, parent):
        super().__init__(
            origin=(-0.5, -0.5),
            scale=(parent.scale_x * 0.35, parent.scale_y * 0.2),
            position=window.bottom_left if not Game.testing() else (-0.5, -0.5),
            parent=parent
        )
        self._health_bar = HealthBar(
            max_value=100,
            scale=(1, 0.3),
            position=(0.1, 0.5),
            parent=self
        )
        self._experience_container = Container(
            position=(0, 1),
            scale=(1, 1),
            parent=self._health_bar
        )
        self.effects_container = EffectsContainer(self)
        self._level = Text(
            "",
            position=(0.9, -0.5),
            origin=(0, 0),
            color=rgb(0, 0, 0),
            scale=(3.3, 30),
            parent=self._experience_container
        )
        self._experience_bar = ExperienceBar(
            max_value=100,
            scale=(0.8, 1),
            value=0,
            position=(0, 0.1),
            parent=self._experience_container
        )
        self._health_bar.text_entity.scale_x *= 1.5
        self._experience_bar.text_entity.scale_x *= 1.5

    def update_data(self, player):
        self._health_bar.max_value = int(player.stats.health.get_value())
        self._health_bar.value = int(player.stats.health.current_value)
        self._level.text = f"{player.experience.level}"
        self._experience_bar.update_data(player.experience.xp, player.experience.get_xp_required(player.star_rating))

