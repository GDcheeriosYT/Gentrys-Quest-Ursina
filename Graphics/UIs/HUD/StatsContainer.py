from ursina import *

import GameConfiguration
from Graphics.Container import Container


class StatsContainer(Container):
    def __init__(self, parent):
        super().__init__(
            origin=(-0.5, 0.5),
            position=(-0.5, 0.5),
            scale=(0.5, 0.5),
            parent=parent
        )
        self._stats_text = Text(
            "",
            parent=self,
            color=rgb(0, 0, 0),
            position=(0.01, 0.02),
            scale=(2, 2)
        )

    def update_data(self, player):
        self._stats_text.text = player.stats if GameConfiguration.extra_ui_info else ""
