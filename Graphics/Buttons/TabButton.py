from ursina import *


class TabButton(Button):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(
            model='quad',
            origin=(0, 0.5),
            color=rgb(117, 117, 117),
            scale=(0.35, 0.15),
            parent=camera.ui,
            *args,
            **kwargs
        )

        self._text = Text(text, color=rgb(0, 0, 0), position=(0, -0.5), scale=(5, 10), origin=(0, 0), parent=self)

    def update(self):
        if self.hovered:
            self._text.color=rgb(255,255,255)
        else:
            self._text.color=rgb(0,0,0)
