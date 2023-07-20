from ursina import *

import Game
from Location.Map import Map
from GameStates import GameStates


class AreaInfoContainer(Entity):
    def __init__(self, parent: Entity):
        super().__init__(
            parent=parent,
            model=Quad(0.02),
            color=color.gray,
            scale=(0.5, 1),
            position=(1, 0)
        )

        self.area_name = Text(
            "",
            origin=(-0.5, 0),
            position=(-0.48, 0.48),
            scale=(1.5, 1.5),
            parent=self
        )
        self.area_description = Text(
            "",
            origin=(-0.5, 0),
            position=(-0.48, 0.4),
            scale=(1.2, 1.2),
            parent=self
        )
        self.area_difficulty = 0

        self.play_button = Button(
            "play",
            color=color.green,
            position=(0, -0.35),
            scale=(0.2, 0.2),
            parent=self
        )

        self.play_button.on_click = lambda: Game.change_state(GameStates.gameplay)

    def update_area_info(self, area: Map):
        self.area_name.text = area.name
        self.area_description.text = area.description
        self.area_difficulty = area.calculate_difficulty(Game.user.get_equipped_character())
