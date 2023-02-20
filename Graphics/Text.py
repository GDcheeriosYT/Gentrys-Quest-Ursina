from ursina.text import Text
from ursina.entity import Entity
from ursina.color import Color
from typing import Union


class TextEntity(Entity):
    def __init__(self, text: str = "Text", position: tuple = (0, 0), scale: Union[int, float] = 1,
                 color: Color = Color()):
        super().__init__(
            model=Text(text),
            color=color,
            scale=scale,
            position=position
        )
