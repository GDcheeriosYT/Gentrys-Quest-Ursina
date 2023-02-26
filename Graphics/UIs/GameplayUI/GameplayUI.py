from Entity.Character.Character import Character
from ursina import *
from ursina.prefabs.health_bar import HealthBar


class GameplayUI:
    def __init__(self, player:Character):
        self.player = player

        # bar container setup
        self.bars_container = Entity(model="quad", origin=(0, 0.5), scale=(0.4, 0.2), position=(0, 0.5), parent=camera.ui)
        self.health_bar = HealthBar(max_value=self.player.stats.health.get_value(), position=(0, -0.45), parent=self.bars_container)
        self.experience_container = Entity(model="quad", position=(0, 0.25), parent=self.bars_container)
        self.level = Text(f"{self.player.experience.level}{f'/{self.player.experience.limit}' if self.player.experience.limit else ''}", position=(0, 0), origin=(0.5, 0), parent=self.experience_container)
        self.experience_bar = HealthBar(max_value=self.player.experience.get_xp_required(self.player.star_rating), value=self.player.experience.xp, position=(0, 0))

    def update_data(self):
        # bars container info update
        self.health_bar.max_value = self.player.stats.health.get_value()
        self.health_bar.value = self.player.stats.health.current_value
        self.level.text = self.player.experience.level
        self.experience_bar.max_value = self.player.experience.get_xp_required(self.player.star_rating)
        self.experience_bar.value = self.player.experience.xp

    def highlight_containers(self):
        self.bars.color = color.rgba(100, 100, 100, 60)