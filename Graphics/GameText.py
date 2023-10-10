from ursina import Text
import GameConfiguration


class GameText(Text):
    def __init__(self, text: str = " ", **kwargs):
        super().__init__(
            text,
            font=GameConfiguration.font,
            **kwargs
        )
