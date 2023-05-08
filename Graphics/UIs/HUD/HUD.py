from ursina import *
from ...Container import Container
from .StatsContainer import StatsContainer
from .StatusBars import StatusBars
from Entity.Character.Character import Character


class HUD(Container):
    def __init__(self, player: Character):
        super().__init__()
        self.player = player
        self._status_bars = StatusBars()
        self._stats_container = StatsContainer()

        self.player.on_add_xp += self.update_status_bars
        self.player.on_heal += self.update_status_bars
        self.player.on_damage += self.update_status_bars
        self.player.on_level_up += self.update_status_bars

        self.player.on_level_up += self.update_stats_container

    def update_status_bars(self):
        self._status_bars.update_data(self.player)

    def update_stats_container(self):
        self._stats_container.update_data(self.player)

    def end(self):
        destroy(self)
