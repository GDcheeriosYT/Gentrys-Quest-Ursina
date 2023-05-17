from ursina import *


class TextContainer(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model='quad',
            position=(0, -0.5),
            origin=(0, -0.5),
            scale=(1, 0.3),
            color=color.gray,
            parent=camera.ui,
            *args,
            **kwargs
        )

        self._text = Text("", position=(-0.5, 0.5), parent=self)

    def preview(self):
        pass
