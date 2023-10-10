from ursina import Button, Text

import Game
import GameConfiguration


class GameButton(Button):
    def __init__(self, text: str = " ", **kwargs):
        super().__init__(
            text,
            **kwargs
        )

        try:
            self.text_entity.font = GameConfiguration.font
        except AttributeError as e:
            self.text_entity = Text()
            Game.exception_handler.handle_exception(e)
