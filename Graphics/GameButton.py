from ursina import Button

import GameConfiguration


class GameButton(Button):
    def __init__(self, text: str = " ", **kwargs):
        super().__init__(
            text,
            **kwargs
        )

        self.text_entity.font = GameConfiguration.font
