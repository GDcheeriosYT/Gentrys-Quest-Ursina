from Entity.Character.Character import Character
from ursina import *
from ursina.prefabs.health_bar import HealthBar
from Graphics.Container import Container


class GameplayUI:
    def __init__(self, player:Character):
        self.player = player

    # bar container setup
    @property
    def bars_container(self) -> Container:
        return Container(origin=(0, 0.5), scale=(0.4, 0.2), position=(0, -1))

    @property
    def health_bar(self) -> HealthBar:
        return HealthBar(max_value=self.player.stats.health.get_value(), position=(0, -0.45), parent=self.bars_container)

    @property
    def experience_container(self) -> Container:
        return Container(position=(0, 0.25))

    @property
    def level(self) -> Text:
        return Text(f"{self.player.experience.level}{f'/{self.player.experience.limit}' if self.player.experience.limit else ''}", position=(-0.4, 0), origin=(0.5, 0), parent=self.experience_container)

    @property
    def experience_bar(self) -> HealthBar:
        return HealthBar(max_value=self.player.experience.get_xp_required(self.player.star_rating), value=self.player.experience.xp, position=(0, 0))

    def update_data(self):
        # bars container info update
        self.health_bar.max_value = self.player.stats.health.get_value()
        self.health_bar.value = self.player.stats.health.current_value
        self.level.text = self.player.experience
        self.experience_bar.max_value = self.player.experience.get_xp_required(self.player.star_rating)
        self.experience_bar.value = self.player.experience.xp
