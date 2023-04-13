from Entity.Character.Character import Character
from Entity.Character.ExperienceBar import ExperienceBar
from ursina import *
from ursina.prefabs.health_bar import HealthBar
from Graphics.Container import Container
from time import perf_counter


class GameplayUI:
    def __init__(self, player:Character):
        self.player = player
        self._bars_container = Container(
            origin=(0, -0.5),
            scale=(0.8, 0.2),
            position=(0, -0.5)
        )
        self._health_bar = HealthBar(
            max_value=self.player.stats.health.get_value(),
            scale=(1, 0.3),
            position=(-0.5, 0.5),
            parent=self._bars_container,
        )
        self._experience_container = Container(
            position=(0, 0.95),
            parent=self.bars_container
        )
        self._level = Text(
            f"lvl. {self.player.experience.level}{f'/{self.player.experience.limit}' if self.player.experience.limit else ''}",
            position=(-0.45, 0),
            origin=(0.5, 0.5),
            color=rgb(0, 0, 0),
            scale=(4, 12),
            parent=self.experience_container
        )
        self._experience_bar = ExperienceBar(
            max_value=self.player.experience.get_xp_required(self.player.star_rating),
            scale=(0.9, 0.3),
            value=self.player.experience.xp,
            position=(-0.41, 0),
            parent=self.experience_container
        )

    # bar container setup
    @property
    def bars_container(self) -> Container:
        return self._bars_container

    @property
    def health_bar(self) -> HealthBar:
        return self._health_bar

    @property
    def experience_container(self) -> Container:
        return self._experience_container

    @property
    def level(self) -> Text:
        return self._level

    @property
    def experience_bar(self) -> ExperienceBar:
        return self._experience_bar

    def update_data(self):
        # bars container info update
        self.health_bar.max_value = self.player.stats.health.get_value()
        self.health_bar.value = self.player.stats.health.current_value
        self.level.text = f"lvl. {self.player.experience.level}"
        self.experience_bar.update_data(self.player.experience.xp, self.player.experience.get_xp_required(self.player.star_rating))
