from ursina import *
from ...Container import Container
from .StatsContainer import StatsContainer
from .StatusBars import StatusBars
from .SkillsContainer import SkillsContainer
from .EffectsContainer import EffectsContainer
from Entity.Character.Character import Character
from ...TextStyles.ScoreText import ScoreText


class HUD(Container):
    def __init__(self, player: Character, parent=camera.ui):
        super().__init__(parent=parent)
        self.player = player
        self._status_bars = StatusBars(self)
        self._score_display = ScoreText(position=(0.5, 0.5), origin=(0.55, 0.55), scale=(2, 2), parent=self)
        self._stats_container = StatsContainer(self)
        self._skills_container = SkillsContainer(self.player, self)
        self._effects_container = EffectsContainer(self)
        self._effects_container.parent = self._status_bars

        self.player.on_add_xp += self.update_status_bars
        self.player.on_heal += self.update_status_bars
        self.player.on_damage += self.update_status_bars
        self.player.on_update_stats += self.update_status_bars
        self.player.on_affected += lambda: self._effects_container.update_data(self.player.effects)

        self.update_status_bars()

    def update_status_bars(self):
        self._status_bars.update_data(self.player)

    def update_stats_container(self):
        self._stats_container.update_data(self.player)

    def hide_elements(self):
        self._status_bars.disable()
        self._stats_container.disable()
        self._skills_container.disable()
        self._score_display.disable()

    def show_elements(self):
        self._status_bars.enable()
        self._stats_container.enable()
        self._skills_container.enable()
        self._score_display.enable()

    def end(self):
        self.player.on_add_xp -= self.update_status_bars
        self.player.on_heal -= self.update_status_bars
        self.player.on_damage -= self.update_status_bars
        self.player.on_update_stats -= self.update_status_bars  # remove the update event
        destroy(self._status_bars)
        destroy(self._stats_container)
        destroy(self._skills_container)
        destroy(self._effects_container)
        destroy(self._score_display)
        destroy(self)

        # destroy children and self

    def update(self):
        self.update_stats_container()
