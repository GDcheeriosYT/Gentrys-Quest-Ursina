from ursina import *


class TestSliderVariable(Slider):
    def __init__(self, text: str, min, max, default):
        super().__init__(
            min=min,
            max=max,
            default=default,
            text=text,
            scale=(1, 1)
        )

        self.name = text

        self.disable()
