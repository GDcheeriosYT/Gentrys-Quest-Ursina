from ursina import *
from typing import Union


class TextContainer(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model=Quad(radius=0.06),
            position=(0, -0.5),
            origin=(0, -0.5),
            scale=(1, 0.3),
            color=rgb(17, 17, 17, 117),
            parent=camera.ui,
            *args,
            **kwargs
        )

        self._text = Text("", position=(-0.5, 0.7), scale=(2, 4), parent=self)
        self.disable()

    def set_text(self, text: str, time: Union[int, float]):
        self.enable()
        self._text.text = text
        invoke(self.disable, delay=time)

    def schedule_text(self, text: str, time: Union[int, float], time_fade: Union[int, float]):
        invoke(lambda: self.set_text(text, time_fade), delay=time)
