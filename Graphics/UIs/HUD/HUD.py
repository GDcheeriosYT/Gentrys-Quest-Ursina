from ursina import *
from ...Container import Container
from .StatsContainer import StatsContainer
from .StatusBars import StatusBars
from .SkillsContainer import SkillsContainer
from Entity.Character.Character import Character


class HUD(Container):
    def __init__(self, player: Character):
        super().__init__()
        self.player = player
        self._status_bars = StatusBars()
        self._stats_container = StatsContainer()
        self._skills_container = SkillsContainer(self.player)

        self.player.on_add_xp += self.update_status_bars
        self.player.on_heal += self.update_status_bars
        self.player.on_damage += self.update_status_bars
        self.player.on_update_stats += self.update_status_bars

    def update_status_bars(self):
        self._status_bars.update_data(self.player)

    def update_stats_container(self):
        self._stats_container.update_data(self.player)

    def hide_elements(self):
        self._status_bars.disable()
        self._stats_container.disable()
        self._skills_container.disable()

    def show_elements(self):
        self._status_bars.enable()
        self._stats_container.enable()
        self._skills_container.enable()

    def end(self):
        destroy(self._status_bars)
        destroy(self._stats_container)
        destroy(self._skills_container)
        destroy(self)

    def update(self):
        self.update_stats_container()
