from Entity.Character.Character import Character
from Entity.Character.ExperienceBar import ExperienceBar
from ursina import *
from ursina.prefabs.health_bar import HealthBar
from Graphics.Container import Container


class GameplayUI:
    def __init__(self, player:Character):
        self.player = player

    # bar container setup
    @property
    def bars_container(self) -> Container:
        return Container(
            origin=(0, -0.5),
            scale=(0.8, 0.2),
            position=(0, -0.5)
        )

    @property
    def health_bar(self) -> HealthBar:
        return HealthBar(
            max_value=self.player.stats.health.get_value(),
            scale=(1, 0.3),
            position=(-0.5, 0.5),
            parent=self.bars_container
        )

    @property
    def experience_container(self) -> Container:
        return Container(
            position=(0, 0.95),
            parent=self.bars_container
        )

    @property
    def level(self) -> Text:
        return Text(
            f"{self.player.experience.level}{f'/{self.player.experience.limit}' if self.player.experience.limit else ''}",
            position=(-0.5, 0),
            origin=(-0.5, 0.5),
            color=rgb(0, 0, 0),
            scale=(4, 10),
            parent=self.experience_container
        )

    @property
    def experience_bar(self) -> ExperienceBar:
        return ExperienceBar(
            max_value=self.player.experience.get_xp_required(self.player.star_rating),
            scale=(0.9, 0.3),
            value=self.player.experience.xp,
            position=(-0.41, 0),
            parent=self.experience_container
        )

    def update_data(self):
        # bars container info update
        self.health_bar.max_value = self.player.stats.health.get_value()
        self.health_bar.value = self.player.stats.health.current_value
        self.level.text = self.player.experience.level
        self.experience_bar.update_data(self.player.experience.xp, self.player.experience.get_xp_required(self.player.star_rating))
