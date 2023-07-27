from ursina import *


class Container(Entity):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(
            parent=camera.ui if not parent else parent,
            *args,
            **kwargs
        )

        self.original_color = self.color
        self.highlighted = False

    def input(self, key):
        if key == "h":
            if self.highlighted:
                self.unhighlight()
            else:
                self.highlight()

    def highlight(self):
        self.color = rgb(17, 17, 17, 125)
        self.highlighted = True

    def unhighlight(self):
        self.color = self.original_color
        self.highlighted = False
