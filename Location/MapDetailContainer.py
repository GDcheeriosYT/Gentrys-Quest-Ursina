from ursina import *

from Graphics.Containers.DirectionalContainer import DirectionalContainer


class MapDetailContainer(Button):
    def __init__(self, preview: Entity, info: Text, *args, **kwargs):
        super().__init__(
            color=color.clear,
            *args,
            **kwargs
        )

        self.container = DirectionalContainer(True, [preview, info], parent=self)
